"""Offline structural check of the own practice pack, not UI/runtime acceptance."""
from pathlib import Path
import argparse,json,hashlib
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(folder):
 d=Path(folder).resolve();ui=json.loads((d/'QWEN21-KOLORIEREN-WORKFLOW.json').read_text(encoding='utf-8'));api=json.loads((d/'QWEN21-KOLORIEREN-API.json').read_text(encoding='utf-8'))
 by={n['id']:n for n in ui['nodes']};assert len(by)==len(ui['nodes'])==8 and set(by)==set(range(1,9))
 classes={1:'UNETLoader',2:'CLIPLoader',3:'VAELoader',4:'TextEncodeQwenImage21',5:'KSampler',6:'VAEDecode',7:'SaveImage',8:'LoadImage'}
 for nid,typ in classes.items():assert by[nid]['type']==api[str(nid)]['class_type']==typ
 expected={(2,0,4,0,'CLIP'),(8,0,4,1,'IMAGE'),(3,0,4,2,'VAE'),(1,0,5,0,'MODEL'),(4,0,5,1,'CONDITIONING'),(4,1,5,2,'CONDITIONING'),(4,2,5,3,'LATENT'),(5,0,6,0,'LATENT'),(3,0,6,1,'VAE'),(6,0,7,0,'IMAGE')}
 assert len(ui['links'])==10 and len({l[0] for l in ui['links']})==10 and {tuple(l[1:]) for l in ui['links']}==expected
 for lid,origin,out_index,target,in_index,typ in ui['links']:
  o=by[origin]['outputs'][out_index];i=by[target]['inputs'][in_index]
  assert lid in o['links'] and i['link']==lid and o['type']==i['type']==typ
  assert api[str(target)]['inputs'][i['name']]==[str(origin),out_index]
 for node in by.values():
  for index,i in enumerate(node['inputs']):assert sum(l[3]==node['id'] and l[4]==index for l in ui['links'])==1
  for index,o in enumerate(node['outputs']):assert set(o.get('links') or [])=={l[0] for l in ui['links'] if l[1]==node['id'] and l[2]==index}
 assert by[1]['widgets_values']==[api['1']['inputs']['unet_name'],api['1']['inputs']['weight_dtype']]
 assert by[2]['widgets_values']==[api['2']['inputs']['clip_name'],api['2']['inputs']['type'],api['2']['inputs']['device']]
 assert by[3]['widgets_values']==[api['3']['inputs']['vae_name']]
 assert by[4]['widgets_values']==[api['4']['inputs']['prompt'],api['4']['inputs']['negative_prompt'],api['4']['inputs']['resolution']]
 k=api['5']['inputs'];assert by[5]['widgets_values']==[k['seed'],'fixed',k['steps'],k['cfg'],k['sampler_name'],k['scheduler'],k['denoise']]
 assert by[7]['widgets_values']==[api['7']['inputs']['filename_prefix']]
 assert by[8]['widgets_values']==[api['8']['inputs']['image'],'image']
 assert (d/'PROMPT.txt').read_text(encoding='utf-8').strip()==api['4']['inputs']['prompt']
 h=json.loads((d/'HERKUNFT.json').read_text(encoding='utf-8'));image=d/api['8']['inputs']['image'];assert image.name==h['file'] and sha(image)==h['sha256']
 return {'structural_check':'passed','nodes':8,'connections':10,'api_ui_parameters_match':True,'synthetic_input_sha256':sha(image),'image_changed':False,'server_contacted':False,'model_loaded':False,'actual_UI_import':'not tested','actual_colorization':'not executed','all_model_files_on_viewer_machine':'not checked'}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--folder',default='.');p.add_argument('--output',required=True);a=p.parse_args();o=Path(a.output).resolve()
 if o.exists():raise SystemExit('Existing report preserved; choose a new file')
 try:result=check(a.folder)
 except (AssertionError,KeyError,IndexError,ValueError,OSError) as e:raise SystemExit('Pack check failed: '+type(e).__name__+' '+str(e))
 o.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
