#!/bin/bash
#SBATCH -J RSF_model                           # Job name
#SBATCH -N1 --ntasks-per-node=1                 # Number of nodes and cores per node required
#SBATCH --mem-per-cpu=4G                        # Memory per core
#SBATCH  --time=24:00:00                        # Duration of the job (Ex: 10 mins)
#SBATCH -o run_RSF_model-%j.out                        # Combined output and error messages file
#SBATCH --mail-type=FAIL              # Mail preferences

 
python https://urldefense.proofpoint.com/v2/url?u=http-3A__rsf-5Fmodel-5Fvariable-5Fexplainer.py&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=RIrrLfyJMToiINJPjKSWV9FHYOQhG2tx3dHnBAzm4E4&e=  $1 $2 $3 $4 $5

# $1 filename to read (.csv)
# $2 name of status variable "MET_STATUS" or "DMETS_DX_LUNG"
# $3 name of time variable "TIME_TO_MET_OR_NOT_MET_AFTER_SEQUENCING"
# $4 name for the file (all_metastases or lung_metastases)
# $5 seed


