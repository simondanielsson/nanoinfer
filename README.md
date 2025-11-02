# nanoinfer

`nanoinfer` is a minimal and lightweight LLM inference engine, mostly for educational purposes. It implements the following features:

- [ ] Basic features (generate tokens from pure SDA LLM, concurrent prefill + decode, ...)
- [ ] Continuous batching
- [ ] Automatic prefix caching
- [ ] PD disagg
- [ ] TP

## Installation

For developers:

```bash
uv venv --python 3.13 --seed
source .venv/bin/activate
make install_dev
```

## TODO checklist

- [ ] Finish up basic engine/model runner/scheduler
- [ ] Build KV paging data structure
- [ ] Add one model architecture (PyTorch), one with pure SDA attn (say TinyLlama-1.1B or OPT-125M).
- [ ] Patch the model forward with a `paged_kv_gather` Triton kernel op to gather the ragged KV cache so we can then run FA. Copy the prefill'ed KV cache into pages for now.
- [ ] Rewrite `paged_kv_gather` in CUDA/C++.
- [ ] Write a `paged_kv_scatter_prefill` Triton kernel to store the prefill output (KV cache) into ragged pages.

Stretch goals:

- [ ] Prefix sharing (COW) using block refcounts.
- [ ] Persistent decode kernels
