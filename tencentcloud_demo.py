from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models

try:
    cred = credential.Credential("AKIDCHkFfwgQehbVSEwIaihWxSqZFm8WYoAO", "e9j9AziIk4EIEtPn3DD3Ufu0KFxWyMae")
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    req = models.DescribeInstancesRequest()
    resp = client.DescribeInstances(req)

    print(resp.to_json_string())
except TencentCloudSDKException as err:
    print(err)