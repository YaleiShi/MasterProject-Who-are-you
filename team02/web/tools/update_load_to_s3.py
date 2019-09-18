import boto3





localPath = "/Users/zhangyousong/Downloads/data/lisa/data/timit/raw/TIMIT/TRAIN/DR1/FKFB0/SI978.mp3"
path = "DR1/FKFB0/SI978.mp3"
client = boto3.client('s3', region_name='us-west-1')
client.upload_file(localPath, 'audio2timit', path,
                       ExtraArgs={'ContentType': 'audio/mp3', 'ACL': 'public-read'})
