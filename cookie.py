from urllib import request
from urllib import parse

url = 'https://user.qzone.qq.com/4244722'

header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'cookie':'RK=Jfuz1FnqMD; eas_sid=M1z5M1z0x5n8b3Q72287Z7X2s6; pgv_pvi=1293990912; pgv_pvid=2062955225; ptcz=0ec87264d14eaca3bfa3c679094d2a3466ddb99c455b02800fa54d384024db8d; o_cookie=347543091; _ga=GA1.2.790552441.1527388984; pgv_si=s3060019200; pt2gguin=o0004244722; uin=o0004244722; skey=@utSc6cStg; ptisp=ctc; p_uin=o0004244722; pt4_token=xQNH7FqkaNcZ0fqDdxHon1QXywet6VFNcEuxoQtRDK4_; p_skey=SHWdFUztkOAcLx3R*7fXDywIqa7T9QZhrOJz4FcSQkY_; welcomeflash=4244722_99106; hibext_instdsigdipv2=1; qz_screen=1920x1080; pgv_info=ssid=s3698724560; 4244722_todaycount=0; 4244722_totalcount=10654; QZ_FE_WEBP_SUPPORT=1'
}

req=request.Request(url,headers=header)
resp=request.urlopen(req)
result = resp.read()
with open('qq.html','w') as fp:
    # write函数必须写入一个string类型的函数
    # resp.read()读出来的是一个bytes类型的数据
    # bytes->decode->str
    # str->encode->bytes
    fp.write(result.decode('utf-8'))
