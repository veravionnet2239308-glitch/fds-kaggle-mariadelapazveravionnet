from sklearn.ensemble import ExtraTreesClassifier

def build_model():
    """
    Returns the final ExtraTreesClassifier configuration
    used for the Kaggle competition submissions.
    """
    model = ExtraTreesClassifier(
        n_estimators=1200,
        max_depth=None,
        min_samples_leaf=2,
        max_features="sqrt",
        bootstrap=False,
        n_jobs=-1,
        random_state=42,
    )
    return model
