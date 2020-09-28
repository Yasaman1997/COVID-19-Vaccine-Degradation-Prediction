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
| 35-OpenVaccine-SN_filter clean data | ??? | 0.222115 | 0.25790 | ??? |
| 36-OpenVaccine-signal_to_noise clean data | ??? | 0.221072 | 0.25487 | ??? |
| 37-OpenVaccine-CNN-LSTM | ??? | 0.229228 | ??? | ??? |
| 38-OpenVaccine-Multi-output mse loss | ??? | 0.222786 | 0.25513 | ??? |
| 39-OpenVaccine-Multi-output weighted loss | ??? | 0.222065 | 0.25374 | ??? |
| 40-OpenVaccine-bpps scaled | ??? | 0.222417 | 0.25344 | ??? |
| 41-OpenVaccine-weighted samples | ??? | 0.218368 | 0.25216 | ??? |
| 42-OpenVaccine-Conv categorical features | ??? | 0.219478 | 0.25539 | ??? |
| 43-OpenVaccine-Numerical features and conv | ??? | 0.219408 | ??? | ??? |
| 44-OpenVaccine-41 SN clean data | ??? | 0.223645 | ??? | ??? |
| 45-OpenVaccine-Embedding-GRU | ??? | 0.221293 | 0.25610 | ??? |
| 46-OpenVaccine-Embedding-GRU sample weight v2 | ??? | 0.221598 | 0.25613 | ??? |
| 47-OpenVaccine-Embedding-GRU 60 epochs | ??? | 0.222528 | 0.25616 | ??? |
| 48-OpenVaccine-Embedding-GRU sample weight v3 | ??? | 0.222777 | 0.25617 | ??? |
| 49-OpenVaccine-Embedding-GRU public | ??? | 0.223156 | ??? | ??? |
| 50-OpenVaccine-Embedding-GRU public v2 | ??? | 0.223657 | ??? | ??? |
| 51-OpenVaccine-Embedding-GRU public v3 | ??? | 0.223291 | ??? | ??? |
| 52-OpenVaccine-Embedding-GRU refactor | ??? | 0.222097 | ??? | ??? |
| 53-OpenVaccine-Embedding-CNN-GRU | ??? | 0.222078 | 0.25341 | ??? |
| 54-OpenVaccine-Embedding-CNN-GRU 2 blocks | ??? | 0.220330 | 0.25274 | ??? |
| 55-OpenVaccine-Embedding-Wavenet-GRU | ??? | 0.223454 | ??? | ??? |
| 56-OpenVaccine-Embedding-GRU param | ??? | 0.223220 | ??? | ??? |
| 57-OpenVaccine-Embedding-CNN-GRU v2 | ??? | 0.221438 | 0.25429 | ??? |
| 58-OpenVaccine-Embedding-CNN-GRU weighted loss | ??? | 0.222899 | ??? | ??? |
| 59-OpenVaccine-CNN-GRU weighted samples v2 | ??? | 0.219665 | 0.25234 | ??? |
| 60-OpenVaccine-CNN-BiGRU self-attention | ??? | 0.220485 | 0.25230 | ??? |
| 61-OpenVaccine-Seq2Seq | ??? | 0.219816 | 0.25299 | ??? |
| 62-OpenVaccine-Seq2Seq Luong Attention | ??? | 0.221843 | ??? | ??? |
| 63-OpenVaccine-Seq2Seq no initial_state | ??? | 0.220592 | 0.25295 | ??? |
| 64-OpenVaccine-TF Luong Attention | ??? | 0.221517 | 0.25265 | ??? |
| 65-OpenVaccine-TF Bahdanau AdditiveAttention | ??? | 0.220556 | 0.25205 | ??? |
| 66-OpenVaccine-TF Bahdanau Attention batchnorm | ??? | 0.234599 | ??? | ??? |
| 67-OpenVaccine-TF Bahdanau AdditiveAttention bs32 | ??? | 0.219054 | 0.25120 | ??? |
| 68-OpenVaccine-TF Bahdanau Attention safe features | ??? | 0.220838 | 0.25355 | ??? |
| 69-OpenVaccine-TF Bahdanau Attention no mean | ??? | 0.220008 | 0.25111 | ??? |
| 70-OpenVaccine-TF Bahdanau Attention spatial_025 | ??? | 0.219605 | ??? | ??? |
| 71-OpenVaccine-Embed-GRU-SelfAttention spatial | ??? | 0.222202 | 0.25305 | ??? |
| 72-OpenVaccine-SharedEmbed-GRU-SelfAttention spati | ??? | 0.221293 | 0.25223 | ??? |
| 73-OpenVaccine-TF Bahdanau Attention SN_filter | ??? | 0.223864 | ??? | ??? |
| 74-OpenVaccine-Embedding-Conv-BiGRU | ??? | 0.220054 | 0.25338 | ??? |
| 75-OpenVaccine-6xConv-BiGRU | ??? | 0.218725 | 0.25180 | ??? |
| 76-OpenVaccine-1xConv-BiGRU | ??? | 0.218959 | 0.25229 | ??? |
| 77-OpenVaccine-6xConv-BiGRU kernel_3 | ??? | 0.218291 | 0.25145 | ??? |
| 78-OpenVaccine-6xConv-2xConv-BiGRU | ??? | 0.219032 | 0.25210 | ??? |
| 79-OpenVaccine-6xConv-1xConv-BiGRU | ??? | 0.218292 | 0.25167 | ??? |
| 80-OpenVaccine-6xConv(swish)-BiGRU | ??? | 0.220396 | ??? | ??? |
| 81-OpenVaccine-6xConv-BiGRU kernel_3 clean valid | ??? | 0.218237 | 0.25146 | ??? |
| 82-OpenVaccine-Embedding-4xConv-BiGRU | ??? | 0.218498 | 0.25219 | ??? |
| 83-OpenVaccine-6xConv-BiGRU-Attention | ??? | 0.220298 | ??? | ??? |
| 84-OpenVaccine-6xConv-BiGRU-AdditiveAttention | ??? | 0.220986 | ??? | ??? |
