import pandas as pd
import boto3
import pandas_redshift as pr
from io import StringIO

def write_dataframe_to_csv_on_s3(dataframe, filename, **kwarg):
    """ Write a dataframe to a CSV on S3 """
    print("Writing {} records to {}".format(len(dataframe), filename))
    path = 'tmp/out.csv'
    dataframe.to_csv(path, sep=";", index=False, decimal = ',', encoding='ISO-8859-1', **kwarg)
    s3_resource = boto3.resource("s3")
    s3_resource.Object('krotonanalytics', filename).upload_file(path)
    print('Done')

def write_dataframe_on_s3(dataframe, filename, parquet=False, **kwarg):
    """ Write a dataframe to a CSV on S3 """
    print("Writing {} records to {}".format(len(dataframe), filename))
    path = 'tmp/out.csv'
    if parquet:
        dataframe.to_parquet(path, index=False, **kwarg)
    else:
        dataframe.to_csv(path, sep=";", index=False, decimal = ',', encoding='ISO-8859-1', **kwarg)
    s3_resource = boto3.resource("s3")
    s3_resource.Object('krotonanalytics', filename).upload_file(path)
    print('Done')
    
def save_partitions(df, filter_dict):
    filter_acumulator = pd.Series(data=False, index=df.index)
    filter_counter = 0
    for file, data_filter in filter_dict.items():

        filter_acumulator = filter_acumulator | data_filter
        filter_counter += data_filter.sum()

    dataframe_list = []
    if filter_acumulator.all() and (filter_counter == df.shape[0]):
        for file, data_filter in filter_dict.items():
            df_output = df[data_filter].copy()
            write_dataframe_to_csv_on_s3(df_output, file)
            dataframe_list.append(df_output)
        return dataframe_list
    else:
        display(filter_acumulator)
        print(filter_counter)
        print(df.shape[0])
        raise Exception('Filters are not a perfect partition')

def salva_csv_no_s3(dataframe,filename):
    """ Write a dataframe to a CSV on S3 """
    print("Writing {} records to {}".format(len(dataframe), filename))
    # Create buffer
    csv_buffer = StringIO()
    # Write dataframe to buffer
    dataframe.to_csv(csv_buffer, sep=";", index=False,encoding = 'latin1',decimal = ',')
    # Create S3 object
    s3_resource = boto3.resource("s3")
    # Write buffer to S3 object
   # newname = 'stakeholders/academico/1_raw/AVALIACAO_CONTINUADA/RELATORIOS_REGIONAL/'+filename
    s3_resource.Object('krotonanalytics', filename).put(Body=csv_buffer.getvalue())
    print('Done')
    
def to_redshift(data_frame, schema_,dbname_,host_,port_,user_,password_,aws_access_key_id_,aws_secret_access_key_,bucket_,subdirectory_):
    print('connect_to_redshift')
    pr.connect_to_redshift(dbname=dbname_,
                           host=host_,
                           port=port_,
                           user=user_,
                           password=password_)
    print('connect_to_s3')
    pr.connect_to_s3(aws_access_key_id=aws_access_key_id_,
                     aws_secret_access_key=aws_secret_access_key_,
                     bucket=bucket_,
                     subdirectory=subdirectory_
                     )
    print('pandas_to_redshift')
    pr.pandas_to_redshift(data_frame=data_frame,
                          index=False,
                          redshift_table_name= schema_,
                          append = False)
    print('fim save_to_redshift')