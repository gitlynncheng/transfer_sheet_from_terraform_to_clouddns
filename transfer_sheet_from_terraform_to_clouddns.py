import csv

zone_name='lynntest'

# record 字串組合
def record_string(record_index,record_sub,record_type,record_rrdata,record_ttl):
    if record_sub == '':
        sub_name="lynntest.com.tw."
    elif record_sub != '':
        sub_name=f"{record_sub}.lynntest.com.tw."
    else :
        print ("ERROR from def record_string")

    record_string_result = f'''resource "google_dns_record_set" "{zone_name}-{record_index}" {{
  managed_zone = google_dns_managed_zone.{zone_name}.name
  name         = "{sub_name}"
  type         = "{record_type}"
  rrdatas      = ["{record_rrdata}"]
  ttl          = {record_ttl}
}}'''
    print(record_string_result)
    return record_string_result

# =============================================================================================================
# =============================================================================================================
# 讀取 CSV 檔案 並產生 terraform 格式
with open('lynntest-zone1.csv', newline='') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 從第11行開始 以迴圈輸出每一列
  for index , row in enumerate(rows):
    if index > 11 :
        #print(index,row)
        # 沒有子網域
        if row[0] == '':
            record_string(record_index=index+1,record_sub='',record_type=row[1],record_rrdata=row[2],record_ttl=300)
        # 有子網域
        elif row[0]!= '':
            record_string(record_index=index+1,record_sub=row[0],record_type=row[1],record_rrdata=row[2],record_ttl=300)
# =============================================================================================================
# =============================================================================================================