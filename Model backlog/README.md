## Model backlog (list of the developed model and metrics)
- **Train** and **validation** are the splits using the train data from the competition.
- The competition metric is **mean columnwise root mean squared error (MCRMSE)**.
- **Public LB** is the Public Leaderboard score.
- **Private LB** is the Private Leaderboard score.

---

## Models

| Model | Train | Validation | Public LB | Private LB |
|-------|-------|------------|-----------|------------|
| 1-OpenVaccine-Baseline | ??? | ??? | 0.28608 | ??? |
| 2-OpenVaccine-Baseline LSTM | ??? | 0.839189 | 0.29807 | ??? |
| 3-OpenVaccine-3 embeddings same encoder | ??? | 0.836436 | 0.28780 | ??? |
| 4-OpenVaccine-3x embeddings & encoder | ??? | 0.836698 | 0.28923 | ??? |
| 5-OpenVaccine-shared embedding | ??? | 0.834937 | 0.28588 | ??? |
| 6-OpenVaccine-Improving CV split | ??? | 0.834937 | 0.28588 | ??? |
| 7-OpenVaccine-StratifiedKFold | ??? | 0.837357 | 0.28798 | ??? |
| 8-OpenVaccine-dataset sampling | ??? | 0.835799 | 0.28460 | ??? |
| 9-OpenVaccine-Clean data | ??? | 0.844611 | 0.27655 | ??? |
| 10-OpenVaccine-Clean datapb baseline | ??? | ??? | 0.26697 | ??? |
| 11-OpenVaccine-Clean data sampling pb baseline | ??? | 1.034164 | ??? | ??? |
| 12-OpenVaccine-signal_to_noise stratify | ??? | 0.838392 | 0.26673 | ??? |
| 13-OpenVaccine-GRU refactor | ??? | 0.839747 | 0.26845 | ??? |
| 14-OpenVaccine-predict 3 targets | ??? | ??? | 0.26920 | ??? |
| 15-OpenVaccine-single target same encoder | ??? | ??? | 0.27134 | ??? |
| 16-OpenVaccine-semantic heads | ??? | 0.838972 | 0.26727 | ??? |
| 17-OpenVaccine-MCRMSE loss | ??? | 0.838957 | 0.26570 | ??? |
| 18-OpenVaccine-MCRMSE loss complete | ??? | 0.823707 | 0.26515 | ??? |
| 19-OpenVaccine-MCRMSE loss complete v2 | ??? | 0.823707 | 0.26515 | ??? |
| 20-OpenVaccine-skip connections | ??? | 0.822709 | 0.26426 | ??? |
| 21-OpenVaccine-dataset sampling 05 | ??? | 0.823902 | 0.26473 | ??? |
| 22-OpenVaccine-dataset sampling 005 | ??? | 0.826481 | 0.26621 | ??? |
| 23-OpenVaccine-bigger model | ??? | 0.820770 | 0.26417 | ??? |
| 24-OpenVaccine-Wave net | ??? | 0.821086 | 0.26420 | ??? |
| 25-OpenVaccine-Wave net v2 | ??? | 0.821211 | 0.26089 | ??? |
| 26-OpenVaccine-LSTM Wave net | ??? | 0.821373 | 0.25983 | ??? |
| 27-OpenVaccine-CNN-GRU | ??? | 0.821590 | 0.26595 | ??? |
| 28-OpenVaccine-CNN-GRU v2 | ??? | 0.821208 | 0.26483 | ??? |
| 29-OpenVaccine-CNN-GRU v3 | ??? | 0.820088 | 0.26465 | ??? |
| 30-OpenVaccine-Feat-CNN-GRU | ??? | 0.819919 | 0.26334 | ??? |
| 31-OpenVaccine-Using bpps | ??? | 0.819762 | 0.25651 | ??? |
| 32-OpenVaccine-Single CNN using bpps | ??? | 0.819833 | ??? | ??? |
| 33-OpenVaccine-Using bpps max and sum | ??? | 0.820465 | ??? | ??? |
| 34-OpenVaccine-Using bpps max, sum and mean | ??? | 0.819293 | ??? | ??? |
