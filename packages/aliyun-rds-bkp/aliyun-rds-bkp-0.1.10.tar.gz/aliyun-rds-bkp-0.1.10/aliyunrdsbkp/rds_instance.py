import json
from datetime import datetime, timedelta

from aliyunsdkrds.request.v20140815 import DescribeBackupsRequest
from aliyunsdkrds.request.v20140815 import DescribeBinlogFilesRequest

from aliyunrdsbkp.db_file import DBFile


class RDSInstance:
    def __init__(self, client, region_id, instance_id):
        self.client = client
        self.region_id = region_id
        self.instance_id = instance_id
        self.host_id = 0

    def get_host_id(self):
        print("Trying to get host id by the most recent full backup...")
        start_time = datetime(2001, 1, 1)
        recent_bkp = self.get_fullbackup_files(start_time, top=1)[0]
        return recent_bkp.get_host_id()

    def get_backup_files(self, backup_type, start_time, end_time=None):
        if backup_type == 'full':
            print("get_fullbackup_files('{}', '{}')".format(start_time, end_time))
            return self.get_fullbackup_files(start_time, end_time)
        elif backup_type == 'binlog':
            print("get_binlog_files('{}', '{}')".format(start_time, end_time))
            return self.get_binlog_files(start_time, end_time)
        else:
            return None

    def get_fullbackup_files(self, start_time, end_time=None, top=0):
        files = list()
        request = DescribeBackupsRequest.DescribeBackupsRequest()
        # Aliyun SDK works on this way: [Backup End Time]
        # BETWEEN [search start time] AND [search end time].
        # And full backup is taken once at most per day.
        # So it is safe to add 1 day on last backup end time as
        # current start time to avoid reundant downloading.
        start_time += timedelta(days=1)
        request.set_StartTime(start_time.strftime("%Y-%m-%dT00:00Z"))
        if end_time:
            search_end_time = end_time
        else:
            search_end_time = datetime.utcnow()
        # Add 1 day to end time because it is exclusive in SDK
        search_end_time += timedelta(days=1)
        request.set_EndTime(search_end_time.strftime("%Y-%m-%dT00:00Z"))
        request.set_DBInstanceId(self.instance_id)
        request.set_PageSize(100)
        read_record_cnt = 0
        page_num = 1
        while True:
            request.set_PageNumber(page_num)
            response = json.loads(
                self.client.do_action_with_exception(request))
            for bkp in response['Items']['Backup']:
                download_url = bkp["BackupDownloadURL"]
                if self.host_id == 0:  # Set host id as per most recent record
                    self.host_id = bkp["HostInstanceID"]
                file_status = 0 if bkp["BackupStatus"] == "Success" else 1
                file_size = bkp["BackupSize"]
                file_start_time = datetime.strptime(bkp["BackupStartTime"],
                                                    "%Y-%m-%dT%H:%M:%SZ")
                file_end_time = datetime.strptime(bkp["BackupEndTime"],
                                                  "%Y-%m-%dT%H:%M:%SZ")
                print(
                    "Region ID:{}, Instance ID:{}, File Type:{},\n"
                    "File Status:{}, Start Time:{}, End Time:{},\n"
                    "Download Link:{}, File Size:{}\n".format(
                        self.region_id,
                        self.instance_id,
                        'full',
                        file_status,
                        file_start_time,
                        file_end_time,
                        download_url,
                        file_size
                    )
                )
                files.append(DBFile(download_url, self.host_id,
                                    self.region_id, self.instance_id,
                                    file_start_time, file_end_time,
                                    file_type='full',
                                    file_status=file_status,
                                    file_size=file_size))
            read_record_cnt += response["PageRecordCount"]
            page_num += 1
            if (
                (top > 0 and read_record_cnt >= top) or
                read_record_cnt >= response["TotalRecordCount"]
            ):
                break
        return files

    def get_binlog_files(self, start_time, end_time=None):
        files = list()
        if self.host_id == 0:  # Set host id if not set before
            self.host_id = self.get_host_id()
        # Aliyun SDK works on this way: [Backup End Time]
        # BETWEEN [search start time] AND [search end time].
        # So it is safe to add 1 sec on last backup end time as
        # current start time to avoid reundant downloading.
        start_time += timedelta(seconds=1)
        request = DescribeBinlogFilesRequest.DescribeBinlogFilesRequest()
        request.set_StartTime(start_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        if end_time:
            request.set_EndTime(end_time.strftime("%Y-%m-%dT%H:%M:%SZ"))
        else:
            request.set_EndTime(
                datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            )
        request.set_DBInstanceId(self.instance_id)
        request.set_PageSize(100)
        read_record_cnt = 0
        page_num = 1
        while True:
            request.set_PageNumber(page_num)
            response = json.loads(self.client.do_action_with_exception(
                request))
            for binlog in response['Items']['BinLogFile']:
                if binlog['HostInstanceID'] == self.host_id:
                    download_url = binlog['DownloadLink']
                    file_size = binlog['FileSize']
                    checksum = binlog['Checksum']
                    file_start_time = datetime.strptime(
                        binlog['LogBeginTime'],
                        "%Y-%m-%dT%H:%M:%SZ")
                    file_end_time = datetime.strptime(
                        binlog['LogEndTime'],
                        "%Y-%m-%dT%H:%M:%SZ")
                    print(
                        "Region ID:{}, Instance ID:{}, File Type:{},\n"
                        "Start Time:{}, End Time:{},\n"
                        "Download Link:{}, File Size:{}\n".format(
                            self.region_id,
                            self.instance_id,
                            'binlog',
                            file_start_time,
                            file_end_time,
                            download_url,
                            file_size
                        )
                    )
                    files.append(DBFile(download_url, self.host_id,
                                        self.region_id, self.instance_id,
                                        file_start_time, file_end_time,
                                        file_type='binlog',
                                        file_size=file_size,
                                        checksum=checksum))
            read_record_cnt += response["PageRecordCount"]
            print("{} records has been read".format(response["PageRecordCount"]))
            print("Total records:{}".format(response['TotalRecordCount']))
            page_num += 1
            if read_record_cnt >= response['TotalRecordCount']:
                break
        return files
