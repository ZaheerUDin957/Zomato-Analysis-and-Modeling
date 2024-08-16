import streamlit as st

def display_metrics(accuracy, precision, recall, f1_score, kappa):
    st.write(f"**Accuracy:** {accuracy:.4f}")
    st.write(f"**Precision:** {precision:.4f}")
    st.write(f"**Recall:** {recall:.4f}")
    st.write(f"**F1 Score:** {f1_score:.4f}")
    st.write(f"**Cohen's Kappa:** {kappa:.4f}")

def Modeling():
    st.sidebar.header("Select Model")
    model = st.sidebar.radio(
        "Choose a model:",
        ("Logistic Regression", "K-Nearest Neighbors", "Decision Tree")
    )

    st.header("Zomato Modeling")

    if model == "Logistic Regression":
        st.subheader("Logistic Regression Results")
        display_metrics(
            accuracy=0.7789,
            precision=0.7702,
            recall=0.7789,
            f1_score=0.7714,
            kappa=0.6583
        )
        st.image("logistic_bar.png", caption="Logistic Regression - Bar Graphs of Evaluation Metrics")
        st.image("logistic_line.png", caption="Logistic Regression - ROC AUC Curve")
    
    elif model == "K-Nearest Neighbors":
        st.subheader("K-Nearest Neighbors Results")
        display_metrics(
            accuracy=0.7119,
            precision=0.7105,
            recall=0.7119,
            f1_score=0.7103,
            kappa=0.5590
        )
        st.image("knn_bar.png", caption="K-Nearest Neighbors - Bar Graphs of Evaluation Metrics")
        st.image("knn_line.png", caption="K-Nearest Neighbors - ROC AUC Curve")
    
    elif model == "Decision Tree":
        st.subheader("Decision Tree Results")
        display_metrics(
            accuracy=0.9811,
            precision=0.9813,
            recall=0.9811,
            f1_score=0.9812,
            kappa=0.9712
        )
        st.image("tree_bar.png", caption="Decision Tree - Bar Graphs of Evaluation Metrics")
        # st.image("tree_line.png", caption="Decision Tree - ROC AUC Curve")

if __name__ == "__main__":
    Modeling()
