# Usage
```
python3.6 main.py {interface name} {start ip} {prefix or netmask} {number of ip} [{operation = add | del}]
```

Start ip is the first ip that we want to use. Then we sequencially add `{number of ip}` ips. Operation can be `add` for adding interfaces, and `del` for deleting them

## Example:

```
python3.6 main.py ens224 10.179.0.10 16 20000
```
