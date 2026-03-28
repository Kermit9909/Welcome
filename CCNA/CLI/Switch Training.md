
__________

## Configure Switches (Practice Time: 3 minutes)

### Configure SW1

```
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW1
SW1(config)# enable secret cisco123
SW1(config)# line console 0
SW1(config-line)# password cisco
SW1(config-line)# login
SW1(config-line)# logging synchronous
SW1(config-line)# exit
SW1(config)# exit
SW1# write
```

### Configure SW2 (Same as SW1)

```
Switch> enable
Switch# configure terminal
Switch(config)# hostname SW2
SW2(config)# enable secret cisco123
SW2(config)# line console 0
SW2(config-line)# password cisco
SW2(config-line)# login
SW2(config-line)# logging synchronous
SW2(config-line)# exit
SW2(config)# exit
SW2# write
```


## Learn Mac Address

- show mac address-table
- clear mac address-table dynamic
- clear mac address-table dynamic interface <int id>

### Speed and Duplex

Check Interface Status

Switch# show int status

* go to global configuration*

conf t 

int f0/1
speed ?


duplex ?

add description

### Interface Range

SW1(config)#interface range f0/5 - 12    **example**
SW1(config-if-range)#description ## not in use ##
SW1(config-if-range)#shutdown

***Enable a bunch of interfaces

SW1(config)#int range f0/5 - 6, f0/9 - 12
SW1(config-if-range)# no shut


