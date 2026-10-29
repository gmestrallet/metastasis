#!/bin/bash
#SBATCH -J feature_ranking                 # Job name
#SBATCH -N1 --ntasks-per-node=1                 # Number of nodes and cores per node required
#SBATCH --mem-per-cpu=4G                        # Memory per core
#SBATCH  --time=24:00:00                        # Duration of the job (Ex: 10 mins)
#SBATCH -o run_feature_ranking-%j.out                        # Combined output and error messages file
#SBATCH --mail-type=FAIL              # Mail preferences

 
python https://urldefense.proofpoint.com/v2/url?u=http-3A__rank-5Ffeatures.py&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ruke0G8_VdThp9RVbctm_2a5mpedj76bmfaKDt7nErk&e=  $1


