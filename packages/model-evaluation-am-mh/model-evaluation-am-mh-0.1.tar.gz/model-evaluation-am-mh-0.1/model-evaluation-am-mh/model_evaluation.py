import sklearn.metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Model:
    
    def __init__(self, dataframe, label_column, prediction_column, probability_column):
        self.data = dataframe
        self.label_column = label_column
        self.prediction_column = prediction_column
        self.probability_column = probability_column
        
        self.label = dataframe[label_column]
        self.prediction = dataframe[prediction_column]
        self.probability = dataframe[probability_column]
        
    def calculate_performance_metrics(self):
        
        accuracy = sklearn.metrics.accuracy_score(self.label, self.prediction)
        f1_score = sklearn.metrics.f1_score(self.label, self.prediction)
        precision = sklearn.metrics.precision_score(self.label, self.prediction)
        recall = sklearn.metrics.recall_score(self.label, self.prediction)
        roc_auc = sklearn.metrics.roc_auc_score(self.label, self.prediction)
        
        tn, fp, fn, tp = sklearn.metrics.confusion_matrix(self.label, self.prediction).ravel()
        
        
        self.accuracy = accuracy
        self.f1_score = f1_score
        self.precision = precision
        self.recall = recall
        self.roc_auc = roc_auc
        
        self.true_negative = tn
        self.false_positive = fp
        self.false_negative = fn
        self.true_positive = tp
        
    def generate_performance_report(self):
        
        self.calculate_performance_metrics()
        
        performance_dictionary = {'accuracy':self.accuracy, 
                                  'precision': self.precision, 
                                  'recall':self.recall, 
                                  'f1_score':self.f1_score,
                                  'roc_auc': self.roc_auc,
                                  'true_negative': self.true_negative,
                                  'false_positive': self.false_positive,
                                  'false_negative': self.false_negative,
                                  'true_positive': self.true_positive,
                                 }
        
        return(performance_dictionary)
        
        
    def get_best_cutoff(self, metric = 'F1'):
        
        """This function gets the max f1score by testing the probability threshold
        
        Inputs
        - ypred: np.ndarray of predicted probabilities
        - y_test: np.ndarray of actual values
        - min_cutoff: minimum value to try for the probability threshold
        - max_cutoff: maximum value to try for the probability threshold
        - step_size: size of the steps to search for the best probability threshold

        Outputs
        - maxPos - max cutoff for f_metric
        """
        cutoffs = list(np.arange(0, 1, step=0.01))
        
        if metric.upper() == "ACCURACY":
            metric_score = [sklearn.metrics.accuracy_score(np.where(self.probability >= x, 1., 0.), self.label) for x in cutoffs]

        elif metric.upper() == "PRECISION":
            metric_score = [sklearn.metrics.precision_score(np.where(self.probability >= x, 1., 0.), self.label) for x in cutoffs]

        elif metric.upper() == "RECALL":
            metric_score = [sklearn.metrics.recall_score(np.where(self.probability >= x, 1., 0.), self.label) for x in cutoffs]
            
        elif metric.upper() == "F1":
            metric_score = [sklearn.metrics.f1_score(np.where(self.probability >= x, 1., 0.), self.label) for x in cutoffs]
            
        elif metric.upper() == "ROC_AUC":
            metric_score = [sklearn.metrics.roc_auc_score(np.where(self.probability >= x, 1., 0.), self.label) for x in cutoffs]
            
        else:
            print('Metric not supported, f1 was used')
            metric_score = [sklearn.metrics.f1_score(np.where(self.probability >= x, 1., 0.), self.label) for x in cutoffs]
        
        best_cutoff_index = np.argmax(metric_score)
        best_cutoff = cutoffs[best_cutoff_index]
        
        self.best_cutoff = best_cutoff
        
        return(self.best_cutoff)
        
    def create_lift_table(self):
        temp_df = self.data.copy()
        probability_column = self.probability_column
        label_column = self.label_column
        
        data_length = len(self.data)
   
        temp_df = temp_df.sort_values(by = probability_column, ascending = False)
        temp_df['counter'] = range(1,len(temp_df)+1)
        temp_df['decile'] = pd.cut(temp_df['counter'], bins=10, labels = list(range(1, 11)))

        table_setup = pd.DataFrame(temp_df['decile'].value_counts())
        table_setup['decile_label'] = table_setup.index
        table_setup['pct_clients_per_decile'] = table_setup['decile'] / data_length

        lost_counts = temp_df.groupby(['decile', label_column]).size().reset_index(name='lost_counts')
        lost_counts = lost_counts[lost_counts[label_column]==1]
        lost_counts = lost_counts.drop(label_column, 1)
        lost_counts = lost_counts.append(pd.DataFrame({"decile":[item for item in list(range(1,11)) if item not in list(lost_counts['decile'].sort_values())], 
              "lost_counts": 0}))
        lost_counts['decile'] = lost_counts['decile'].astype('category')

        table_setup_merged = table_setup.merge(lost_counts, left_on='decile_label', right_on = 'decile').sort_values('decile_label')
        table_setup_merged['pct_lost_of_total_lost'] = table_setup_merged['lost_counts'] / table_setup_merged['lost_counts'].sum()
        table_setup_merged.rename(columns={'decile_x': 'rows_in_decile', 'decile_label': 'decile_number','lost_counts': 'actual_count'}, inplace=True)
        
        table_setup_merged.drop('decile_y', axis=1, inplace=True)

        self.lift_table = table_setup_merged
        
        return(self.lift_table)
        
    def plot_lift_chart(self):
        
        temp_df = self.create_lift_table()
        
        fig, ax = plt.subplots()
        ax.plot(list(temp_df['decile_number']),
             list(temp_df['pct_lost_of_total_lost']),
             label = "Percent of Total Label",
             color = "black")
        ax.bar(list(temp_df['decile_number']),
               list(temp_df['pct_clients_per_decile']),
               alpha = 0.3,
               label = "Percent of Total")
        ax.set_xlabel("decile")
        ax.set_ylabel("Percentage")
        ax.set_title("Lift Chart")
        ax.legend()
        plt.show()
        
    def cutoff_chart(self):
        
        probability_column = self.probability_column
        label_column = self.label_column
        
        
        df = pd.DataFrame({'cutoffs':list(np.arange(0, 1, step=.01)),
                           
                           'f1':[sklearn.metrics.f1_score(np.where(self.data[probability_column] >= x, 1., 0.),
                                                          self.data[label_column]) for x in cutoffs],
                           
                           'precision':[sklearn.metrics.precision_score(np.where(self.data[probability_column] >= x, 1., 0.),
                                                                        self.data[label_column]) for x in cutoffs],
                           
                           'recall':[sklearn.metrics.recall_score(np.where(self.data[probability_column] >= x, 1., 0.),
                                                                  self.data[label_column]) for x in cutoffs]})

        fig, ax = plt.subplots()
        ax.plot(list(df['cutoffs']),
                list(df['f1']),
                label = "f1 Scores",
                color = "black")
        ax.plot(list(df['cutoffs']),
                list(df['precision']),
                label = "precision scores",
                color = "Red")
        ax.plot(list(df['cutoffs']),
                list(df['recall']),
                label = "recall scores",
                color = "Green")
        ax.set_xlabel("cutoffs")
        ax.set_ylabel("score")
        ax.set_title("cutoff finder")
        ax.legend()
        plt.show()
        
        