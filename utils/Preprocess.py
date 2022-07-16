from konlpy.tag import Okt

jvm_path = "/Library/Java/JavaVirtualMachines/zulu-15.jdk/Contents/Home/bin/java"
okt = Okt(jvmpath=jvm_path)
text = "아 나는 역시 밤에 일이 잘된다."


print(okt.morphs(text, stem=True))
