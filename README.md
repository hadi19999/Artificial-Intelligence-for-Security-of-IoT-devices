The following repository contains different script to train different models:
    1. train_knn_model.py will train a KNN model without optimization
    2. train_rf_model.py will train a Random Forest model without optimization
    3. train_logistic_regression.py will train a Logistic Regression model without optimization
    4. train_svm.py will train a Support Vector Machine model without optimization

The dataset can be downloaded from: https://data.mendeley.com/datasets/3dhn4xnjxw/1

Dataset Structure:
    Main directory:
        - data:
            - S13_S21
                - I1
                .
                .
                .
                - I10

            - S19_S11
                - I1
                .
                .
                .
                - I10

        - test_data:
            - S13_S21
                - I10
                - I11
                - I12
                
            - S19_S11
                - I10
                - I11
                - I12

The model evaluation is done in evaluate_model.ipynb

Mock run:
    In this directory, we have a mock run of our implementation, currenlty the public key technique used
    is twofish as it is fast and simple, and the model will save the data (CSI and RSS) got from the
    transmitter and after a specific number of packets the receiver will train the model and switch
    to our model for authentication.
    currenlty the transmitter is sending data from a mock_data folder that has random RSS and CSI data
    to let the receiver capture these data to train the model.
    - test_data:
        - S13_S21
            - I1
        - S19_S11
            - I1
    The link is authenticated only for S13_S21 data.
