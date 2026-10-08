# Sources and scope

- Installed ComfyUI TextEncodeQwenImage21 schema and own existing API template, source hashes in PROVENIENZ.json. The UI graph was authored by reducing the installed template to the eight required nodes. JSON/connection/parameter checks are separate from real UI import and image inference.
- https://huggingface.co/Qwen/Qwen-Image-2.1/raw/main/LICENSE — exact Qwen Research Licence must be checked for your intended model-material use; no general commercial permission asserted.
- https://huggingface.co/Qwen/Qwen-Image-Edit-2511 — different model and licence; not interchangeable with the 2.1 template.
- https://github.com/Comfy-Org/ComfyUI/blob/d91ed5f5b7fa60fa18464c2ad7c80254da2f0f29/script_examples/basic_api_example.py — Official API example: File -> Export (API), keyed node objects with class_type and inputs. The supplied UI graph and API prompt use separate formats; practical UI import remains untested. Pinned official source checked 2026-10-08; the former documentation URL returned HTTP 404.
- Own synthetic exercise photograph generated with built-in imagegen; original bytes retained. Visually monochrome RGB with slight channel differences, not a real historical scan. Colors generated later are interpretations. No family photographs, foreign transcripts or third-party archival images redistributed.

Own code/guide licence does not replace model licensing or rights in pictures. The sample is for learning; there is no fresh installation, UI acceptance, runtime execution or performance guarantee.
