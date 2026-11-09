"""Parametric Nebula Vault R1. Units: mm. CadQuery 2.8.
Run from any directory: python model.py. Produces STEP, STL, and a geometry report.
Yonathan’s original design prototype. Fit, strength and servo angles are not bench verified.
"""
from pathlib import Path
import json
import math
import cadquery as cq

HERE = Path(__file__).resolve().parent
W, D, H, WALL = 180.0, 140.0, 90.0, 3.0
SKIRT_CLEARANCE = 0.4
SERVO_X, SERVO_Y = 62.0, -38.0
AXLE_Z = 80.0
RING_X, RING_Y = -38.0, -38.0

def box(x, y, z, dx, dy, dz):
    return cq.Workplane('XY').box(dx, dy, dz).translate((x, y, z + dz / 2))

def cylinder(x, y, z, radius, height):
    return cq.Workplane('XY').circle(radius).extrude(height).translate((x,y,z))

def build():
    # Open shell and full-height side walls; rear port is for the Pico's USB cable.
    body = box(0,0,0,W,D,H).cut(box(0,0,WALL,W-2*WALL,D-2*WALL,H))
    body = body.cut(box(-52,-69,5,18,10,12))
    # Release access at the servo height; finger/tool can rotate the horn with power off.
    body = body.cut(box(62,-69,75,26,12,11))
    body = body.union(box(0,-10,3,174,3,61))
    # Perma-proto platform with four edge retainers (no assumed vendor hole positions).
    for x in (-79, 3):
        body = body.union(box(x,-38,3,3,54,5))
    # Servo shelf; two cable-tie slots avoid reliance on exact mounting ear holes.
    shelf = box(62,-38,48,36,30,3)
    for x in (49,75):
        shelf = shelf.cut(box(x,-38,47,3,24,5))
    body = body.union(shelf).union(box(80,-38,3,5,30,48))
    # Rear captive tongues retain the lift-off lid when the horn is locked.
    for x in (-60,-10):
        body = body.union(box(x,-65,84,22,4,3))
    # Exterior ribs follow the sci-fi panel silhouette and add stiffness.
    for x in (-72,72):
        body = body.union(box(x,69,10,6,3,65))

    lid = box(0,0,H,W,D,3)
    skirt_w = W-2*WALL-2*SKIRT_CLEARANCE
    skirt_d = D-2*WALL-2*SKIRT_CLEARANCE
    skirt = box(0,0,86,skirt_w,skirt_d,4).cut(box(0,0,85,skirt_w-4,skirt_d-4,6))
    # Rear tongues enter windows in the skirt; tilt front up to remove lid.
    for x in (-60,-10):
        skirt = skirt.cut(box(x,-66,83,24,9,5))
    lid = lid.union(skirt)
    # Individual light ports preserve the structural web around the encoder.
    for i in range(12):
        a = math.radians(i*30)
        lid = lid.cut(cylinder(RING_X+15*math.cos(a),RING_Y+15*math.sin(a),89,2.5,6))
    lid = lid.cut(cylinder(RING_X,RING_Y,88,3.7,8))
    # Encoder anti-rotation slot and OLED active window; boards fixed by separate straps.
    lid = lid.cut(box(RING_X-6,RING_Y,88,2.2,3.5,8))
    lid = lid.cut(box(15,-38,89,25,8,6))
    # Rear lid retaining hooks must clear body tongues until tilted into place.
    for x in (-60,-10):
        hook = box(x,-63,81,20,8,2.5).union(box(x,-60,81,20,2,9))
        lid = lid.union(hook)
    # Keeper: vertical wall and overhanging roof. Horn passes below roof at 80..82.
    keeper = box(62,-17,77,18,4,13).union(box(62,-23,83,18,12,3))
    lid = lid.union(keeper)
    # OLED clamp posts and ring retainer posts: M3 pilot holes, self-tap nylon screws.
    for x,y in ((-63,-38),(-13,-38),(15,-53),(15,-23)):
        post = cylinder(x,y,81,3,9).cut(cylinder(x,y,80,1.3,11))
        lid = lid.union(post)
    # Decorative top rails double as protective bumpers; label recesses are real geometry.
    for x in (-80,80):
        lid = lid.union(box(x,0,93,4,122,2))
    lid = lid.cut(box(30,35,92,70,20,2))
    for label,yy in (('NEBULA',39),('VAULT',30)):
        lettering = cq.Workplane('XY').text(label,8,1.1,font='Arial',combine=True).translate((30,yy,92))
        lid = lid.union(lettering)

    diffuser = cylinder(RING_X,RING_Y,93.2,20,1.2).cut(cylinder(RING_X,RING_Y,93,10.3,4))
    # 4 retaining tabs bridge the light-well gap. Thin natural PLA; attach with screws.
    for x in (-63,-13):
        edge = RING_X + (-20 if x < RING_X else 20)
        tab = box((x+edge)/2,RING_Y,93.2,abs(x-edge)+5,5,1.6)
        tab = tab.cut(cylinder(x,RING_Y,92,1.7,5))
        diffuser = diffuser.union(tab)
    # Flat servo horn extension. Attach onto supplied horn with two small cable ties.
    latch = box(62,-31.5,80,8,21,2).union(cylinder(62,-38,80,6,2))
    latch = latch.cut(cylinder(62,-38,79,1.4,4))
    for y in (-34,-29): latch = latch.cut(box(62,y,79,5,1.5,4))
    # Strap for OLED, retained by nylon M3x10 screws in posts.
    oled_strap = box(15,-38,79,8,36,2)
    for y in (-53,-23): oled_strap = oled_strap.cut(cylinder(15,y,78,1.7,4))
    # Custom large dial cap; slide over included knob, use shim if required.
    knob = cylinder(RING_X,RING_Y,94,9,12).cut(cylinder(RING_X,RING_Y,93,7.8,11))
    knob = knob.union(box(RING_X,RING_Y+8,104,2,3,2))
    # Tiny fit coupon lets builder validate 0.2..0.6 radial clearances before body print.
    coupon = box(0,0,0,50,16,3)
    for i,clear in enumerate((0.2,0.3,0.4,0.5,0.6)):
        coupon = coupon.cut(cylinder(-20+10*i,0,-1,3+clear,5))

    return {'body':body,'lid':lid,'diffuser':diffuser,'latch':latch,
            'oled_strap':oled_strap,'dial_cap':knob,'fit_coupon':coupon}

def references():
    # Bounding references, not manufacturer CAD; used only for envelope checking.
    return {
        'servo_envelope':box(62,-38,51,23,12.2,27),
        'perma_proto_envelope':box(-38,-38,8,81,51,1.6),
        'pico_envelope':box(-48,-38,12,21,51,10),
        'oled_envelope':box(15,-38,82,38,12,5),
        'ring_envelope':cylinder(-38,-38,83.3,18.4,6.7).cut(cylinder(-38,-38,83,11.65,9)),
    }

if __name__ == '__main__':
    parts = build()
    report = {'units':'mm','revision':'R1','parts':{},'limitations':[
        'Envelope references are simplified, not vendor-certified CAD.',
        'No physical tolerance, torque, optical diffusion or fatigue validation.',
        'CadQuery source is supplied for Freestyle; no claim of CAD-week eligibility.']}
    assembly = cq.Assembly(name='NebulaVault_R1')
    colors = {'body':(0.10,0.13,0.19),'lid':(0.16,0.20,0.28),'diffuser':(0.3,0.95,0.85),
              'latch':(1,0.55,0.12),'oled_strap':(0.6,0.6,0.7),'dial_cap':(0.35,0.9,0.9)}
    for name, obj in parts.items():
        shape = obj.val()
        cq.exporters.export(obj,str(HERE/(name+'.step')))
        # Print files are translated to the build plate, preserving orientation.
        printable = obj.translate((0,0,-shape.BoundingBox().zmin))
        cq.exporters.export(printable,str(HERE/(name+'.stl')),tolerance=0.1,angularTolerance=0.1)
        bbox = shape.BoundingBox()
        report['parts'][name] = {'valid':shape.isValid(),'solids':len(obj.solids().vals()),
            'volume_mm3':round(shape.Volume(),3),'bounds_mm':[round(bbox.xlen,3),round(bbox.ylen,3),round(bbox.zlen,3)]}
        if name != 'fit_coupon': assembly.add(obj,name=name,color=cq.Color(*colors[name]))
    for name,obj in references().items(): assembly.add(obj,name=name,color=cq.Color(0.4,0.6,0.45,0.5))
    assembly.export(str(HERE/'NebulaVault_R1.step'))
    # Compute tangible model fit facts, not just nominal parameter assertions.
    report['checks'] = {
        'lid_body_intersection_mm3':round(parts['lid'].val().intersect(parts['body'].val()).Volume(),6),
        'latch_body_intersection_mm3':round(parts['latch'].val().intersect(parts['body'].val()).Volume(),6),
        'latch_lid_intersection_mm3':round(parts['latch'].val().intersect(parts['lid'].val()).Volume(),6),
        'skirt_nominal_side_clearance_mm':SKIRT_CLEARANCE,
        'horn_top_to_keeper_roof_mm':1.0,
        'diffuser_lid_intersection_mm3':round(parts['diffuser'].val().intersect(parts['lid'].val()).Volume(),6),
    }
    (HERE/'geometry-report.json').write_text(json.dumps(report,indent=2))
    print(json.dumps(report,indent=2))
