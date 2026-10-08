# This is a anndata tutorial Python script.
# Press ⌃R to execute it or replace it with your code.

import numpy as np
import pandas as pd
import anndata as ad
from scipy.sparse import csr_matrix
from importlib.metadata import version
version("anndata")

def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')

counts = csr_matrix(np.random.poisson(1, size=(100, 2000)), dtype=np.float32)
adata = ad.AnnData(counts)
print(adata)
print(adata.X)

adata.obs_names = [f"Cell_{i:d}" for i in range(adata.n_obs)]
adata.var_names = [f"Gene_{i:d}" for i in range(adata.n_vars)]
print(adata.obs_names[:10])
print(adata.var_names[:10])







