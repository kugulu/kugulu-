from Crypto.Util.number import *

flag = b'NSSCTF{******}'

class LCG:
    def __init__(self, seed, a, b, m):
        self.seed = seed  # 初始种子
        self.a = a  # 乘数
        self.b = b  # 增量
        self.m = m  # 模数

    def generate(self):
        self.seed = (self.a * self.seed + self.b) % self.m
        return self.seed


lcg = LCG(bytes_to_long(flag), getPrime(256), getPrime(256), getPrime(256))

for i in range(getPrime(16)):
    lcg.generate()

print(f'a = {lcg.a}')
print(f'b = {lcg.b}')
print(f'm = {lcg.m}')
print(lcg.generate())


'''
a = 113439939100914101419354202285461590291215238896870692949311811932229780896397
b = 72690056717043801599061138120661051737492950240498432137862769084012701248181
m = 72097313349570386649549374079845053721904511050364850556329251464748004927777
9772191239287471628073298955242262680551177666345371468122081567252276480156
'''