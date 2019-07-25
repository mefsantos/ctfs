#! /usr/bin/python

from pwn import *
from Crypto.Util.number import inverse, long_to_bytes
import primefac
import time as t


def phi(p, q):
	return (p-1) * (q-1)

context.log_level = "critical"

host, port ="2018shell.picoctf.com", 50430

con = remote(host, port)


con.recv()
con.sendline("Y")
con.recv()
con.sendline("8815769761")


con.recv()
con.sendline("Y")
con.recv()
con.sendline("77773")


con.recv()
con.sendline("N")


con.recv()
con.sendline("Y")
con.recv()
con.sendline("6256003596")


con.recv()
con.sendline("Y")
con.recv()
con.sendline("26722917505435451150596710555980625220524134812001687080485341361511207096550823814926607028717403343344600191255790864873639087129323153797404989216681535785492257030896045464472300400447688001563694767148451912130180323038978568872458130612657140514751874493071944456290959151981399532582347021031424096175747508579453024891862161356081561032045394147561900547733602483979861042957169820579569242714893461713308057915755735700329990893197650028440038700231719057433874201113850357283873424698585951160069976869223244147124759020366717935504226979456299659682165757462057188430539271285705680101066120475874786208053")

con.recv()
con.sendline("N")

t.sleep(1)
con.recv()
con.sendline("Y")
con.recv()
con.sendline("1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729")


con.recv()
con.sendline("Y")
# last computation
con.recv()
p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
cipher = 313988037963374298820978547334691775209030794488153797919908078268748481143989264914905339615142922814128844328634563572589348152033399603422391976806881268233227257794938078078328711322137471700521343697410517378556947578179313088971194144321604618116160929667545497531855177496472117286033893354292910116962836092382600437895778451279347150269487601855438439995904578842465409043702035314087803621608887259671021452664437398875243519136039772309162874333619819693154364159330510837267059503793075233800618970190874388025990206963764588045741047395830966876247164745591863323438401959588889139372816750244127256609
e = 65537
n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239

# factorint fails: OverflowError: 'mpz' too large to convert to float
#_, q = primefac.factorint(n).keys() # we already have p
# with factordb.com:
q = 156408916769576372285319235535320446340733908943564048157238512311891352879208957302116527435165097143521156600690562005797819820759620198602417583539668686152735534648541252847927334505648478214810780526425005943955838623325525300844493280040860604499838598837599791480284496210333200247148213274376422459183
d = inverse(e, phi(p, q))
plain = pow(cipher, d, n)

# we dont need to send the line, the answer will say the flag is the plain text
print long_to_bytes(plain)

#con.sendline(str(plain))
#print con.recv()

con.close()