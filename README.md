# metastasis
This program allows to predict the metastasis risk based on clinical data and mutational data from the primary tumor by machine learning approaches.

# Scripts to run RSF variable selection

https://urldefense.proofpoint.com/v2/url?u=http-3A__rsf-5Fmodel-5Fvariable-5Fexplainer.py&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=RIrrLfyJMToiINJPjKSWV9FHYOQhG2tx3dHnBAzm4E4&e= : python file to fit RSF model with 40 random variables
https://urldefense.proofpoint.com/v2/url?u=http-3A__rank-5Ffeatures.py&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ruke0G8_VdThp9RVbctm_2a5mpedj76bmfaKDt7nErk&e= : python file to rank features across 4000 models
https://urldefense.proofpoint.com/v2/url?u=http-3A__run-5Frsf-5Fall.sh&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ncjzi_rPVD6r_G_cKTxWkg_LjIRvJcUDscCYuM3CHds&e= : shell file to run all 4000 models
run_RSF_model.sbatch: sbatch file to launch https://urldefense.proofpoint.com/v2/url?u=http-3A__rsf-5Fmodel-5Fvariable-5Fexplainer.py&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=RIrrLfyJMToiINJPjKSWV9FHYOQhG2tx3dHnBAzm4E4&e= 
run_feature_ranking.sbatch: sbatch file to launch https://urldefense.proofpoint.com/v2/url?u=http-3A__rank-5Ffeatures.py&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ruke0G8_VdThp9RVbctm_2a5mpedj76bmfaKDt7nErk&e= 

python dependencies: python 3.10.10, pandas 1.5.3, numpy 1.26.2, scikit-learn 1.2.2, scikit-survival 0.25.0

1. Run 4000 RSF model for each cancer type
	- all cancer: ./https://urldefense.proofpoint.com/v2/url?u=http-3A__run-5Frsf-5Fall.sh&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ncjzi_rPVD6r_G_cKTxWkg_LjIRvJcUDscCYuM3CHds&e=  data.csv MET TIME_TO_MET_OR_NOT_MET_AFTER_SEQUENCING all 1 4000
	- lung: ./https://urldefense.proofpoint.com/v2/url?u=http-3A__run-5Frsf-5Fall.sh&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ncjzi_rPVD6r_G_cKTxWkg_LjIRvJcUDscCYuM3CHds&e=  datalung.csv DMETS_DX_LUNG TIME_TO_MET_OR_NOT_MET_AFTER_SEQUENCING lung 1 4000
	- liver: ./https://urldefense.proofpoint.com/v2/url?u=http-3A__run-5Frsf-5Fall.sh&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ncjzi_rPVD6r_G_cKTxWkg_LjIRvJcUDscCYuM3CHds&e=  dataliver.csv DMETS_DX_LIVER TIME_TO_MET_OR_NOT_MET_AFTER_SEQUENCING liver 1 4000
	- bone: ./https://urldefense.proofpoint.com/v2/url?u=http-3A__run-5Frsf-5Fall.sh&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ncjzi_rPVD6r_G_cKTxWkg_LjIRvJcUDscCYuM3CHds&e=  databone.csv DMETS_DX_BONE TIME_TO_MET_OR_NOT_MET_AFTER_SEQUENCING bone 1 4000
	- abdomen ./https://urldefense.proofpoint.com/v2/url?u=http-3A__run-5Frsf-5Fall.sh&d=DwIGaQ&c=shNJtf5dKgNcPZ6Yh64b-ALLUrcfR-4CCQkZVKC8w3o&r=nM0y_wOcFHlr-lA2FkRI6KM_1fBYHhqAbty6tWZR_vo&m=wYqMNqWTp_j6vKgVyEPxf9iJDVHADgKd9Jt7_ePwWAxRZqzPZEr9AGcB2lnBbhWW&s=Ncjzi_rPVD6r_G_cKTxWkg_LjIRvJcUDscCYuM3CHds&e=  dataabdomen.csv  DMETS_DX_INTRA_ABDOMINAL TIME_TO_MET_OR_NOT_MET_AFTER_SEQUENCING abdomen 1 4000

2. Generate ranking table
	- all: sbatch run_feature_ranking.sbatch all
	- lung: sbatch run_feature_ranking.sbatch lung
	- liver: sbatch run_feature_ranking.sbatch liver
	- bone: sbatch run_feature_ranking.sbatch bone
	- abdomen: sbatch run_feature_ranking.sbatch abdomen
