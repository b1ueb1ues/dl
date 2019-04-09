import slot 

s = slot.Slots('elisanne')
s.d = slot.d.water.Leviathan()
s.w = slot.WeaponBase()
s.w.wt = 'lance'
s.a = slot.a.VC()+slot.a.Witchs_Kitchen()

print(s.att())
print(s.tmp.a.a)
print(s.att())
print(s.tmp.a.a)

