import sys, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'firmware'))
from core import Vault,TARGETS,DIRECTIONS,PULSES_MS
v=Vault();now=0;trace=[]
def record(action): trace.append(dict(time_ms=now,action=action,phase=v.phase,position=v.position,locked=v.locked,message=v.message))
record('boot');v.press(now);record('arm')
for target,direction in zip(TARGETS,DIRECTIONS):
    count=0
    while v.position!=target or not count:
        now+=80;v.rotate(direction,now);count+=1;record('CW' if direction>0 else 'CCW')
    now+=100;v.press(now);record('confirm')
now+=2600;v.tick(now);record('playback complete')
now+=300;v.press(now);record('first tap')
for gap in PULSES_MS:
    now+=gap;v.press(now);record('next tap')
assert v.phase=='OPEN' and not v.locked
result={'kind':'executed ideal event simulation of firmware/core.py','trace':trace,'physical_hardware':False}
(root/'simulation/solution-trace.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
