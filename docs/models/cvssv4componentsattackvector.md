# CVSSv4ComponentsAttackVector

Indicates the level of access required for an attacker to exploit the vulnerability. The Attack Vector metric is scored in one of four levels: Network (N) – Vulnerabilities with this rating are remotely exploitable, from one or more hops away, up to, and including, remote exploitation over the Internet, Adjacent (A) – A vulnerability with this rating requires network adjacency for exploitation. The attack must be launched from the same physical or logical network, Local (L) – Vulnerabilities with this rating are not exploitable over a network, Physical (P) – An attacker must physically interact with the target system.

## Example Usage

```python
from censys_platform.models import CVSSv4ComponentsAttackVector

value = CVSSv4ComponentsAttackVector.UNKNOWN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `UNKNOWN`  |            |
| `NETWORK`  | network    |
| `ADJACENT` | adjacent   |
| `LOCAL`    | local      |
| `PHYSICAL` | physical   |