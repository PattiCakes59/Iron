def fit_n_run_model(var):
    XTR = X_train[var]
    XTST = X_test[var]
    model = sm.OLS(y_train,sm.add_constant(XTR)).fit()
    train_preds = model.predict(sm.add_constant(XTR))
    test_preds = model.predict(sm.add_constant(XTST))
    return model.summary()  