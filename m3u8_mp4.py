import os,sys,urllib.request
path=sys.path[0]
#url1="http://hknm5s6gzvm5a6wju24.exp.bcevod.com/mda-kd5xwkvqnz9yr4pr/mda-kd5xwkvqnz9yr4pr.m3u8"
#url2="http://hknm5s6gzvm5a6wju24.exp.bcevod.com/mda-kd5xwm5ukr1xyzpz/mda-kd5xwm5ukr1xyzpz.m3u8"
#url1="http://hknm5s6gzvm5a6wju24.exp.bcevod.com/mda-kdcvsm09ru885acf/mda-kdcvsm09ru885acf.m3u8"
#url2="http://hknm5s6gzvm5a6wju24.exp.bcevod.com/mda-kdcvshxyqdkfmfd7/mda-kdcvshxyqdkfmfd7.m3u8"
#url1="https://apd-c90f182ba9ffa6791e58f1c74815058a.v.smtcdns.com/omts.tc.qq.com/ACg9Pl9NYesXkxjJ5JCCbCXkE1418hOY8UStQyqx4ZpA/uwMROfz2r5xgoaQXGdGnC2df64_gcR4DH6oNabw6qBdCnk2E/Gr1lnsLMh-4d1D1GkOc9v_xv6ngickxjHqhrEUcTY9nyEoV1fw_bfS1hUEjQHSxiTcJgQhj1fORSHskB-K_YMWiuXf7TH8kPSmBBbHsNYuzUu532b8DpsK_xY_3IK-B2OnQiU9t9rOs_OrAwky_Y98EnJANz2Hrtn02EFO25_ak/h0939je1is2.321003.ts.m3u8?ver=4"
#
# url1="E:/QQ\SPACE/1415470614/FileRecv/offline.m3u8"
# osmsg=path+"/ffmpeg/bin/ffmpeg -i "+url1 +" -vcodec copy -acodec copy -absf aac_adtstoasc first.mp4"
# os.system(osmsg)
'''
t1="q0939yz28oh.p709.1.mp4"
t2="q0939yz28oh.p709.2.mp4"
t3="q0939yz28oh.p709.3.mp4"
t4="q0939yz28oh.p709.4.mp4"
t5="q0939yz28oh.p709.5.mp4"'''
#osmsg=path+"/ffmpeg/bin/ffmpeg -i "+t5+" -vcodec copy -acodec copy -vbsf h264_mp4toannexb 5.ts"

#osmsg=path+"/ffmpeg/bin/ffmpeg -i \"concat:1.ts\|2.ts\|3.ts\|4.ts\" -acodec copy -vcodec copy -absf aac_adtstoasc second.mp4"
#osmsg=path+"/ffmpeg/bin/ffmpeg -i "+t1+" -i "+t2+" -i "+t3+" -i " + t4 +" -f mp4 -acodec libfaac -vcodec libx264 -sameq second.mp4"

#osmsg=path+"/ffmpeg/bin/ffmpeg –i F:/python_space/bs_project/Coby/002.ts –i F:/python_space/bs_project/Coby/003.ts–i F:/python_space/bs_project/Coby/004.ts–i F:/python_space/bs_project/Coby/001.ts–i F:/python_space/bs_project/Coby/005.ts -f mp4 second.mp4"
#os.system(osmsg)
#url="ffmpeg -i “http://xxxxxx/video/movie.m3u8” -vcodec copy -acodec copy -absf aac_adtstoasc output.mp4"
def getpath():
    path=sys.argv[0]
    i=path.rfind("\\")
    if i == -1:
        i = path.rfind("/")
    return path[:i]
def m4a_to_mp3(url,name,mid):
    path = getpath()
    print(url)
    req = urllib.request.urlopen(url)
    with open(path+"/music/"+mid+".m4a", 'wb') as f:
        f.write(req.read())
    osmsg = path+"/ffmpeg/bin/ffmpeg -i "+path+"/music/"+mid+".m4a "+path+"/music/"+mid+".mp3"
    os.system(osmsg)
    #os.rename(path+"/music/"+mid+".wav",path+"/music/"+name+".wav")
    return path+"/music/"+name+".mp3"
if __name__ == '__main__':
    m4a_to_mp3("https://res.wx.qq.com/voice/getvoice?mediaid=MzA4NTIxMDg5M18yMjQ3NDg0OTAx","first","first")