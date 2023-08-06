from ..imports import *
from .. import utils as U
from ..core import ArrayLearner




class BERTTextClassLearner(ArrayLearner):
    """
    Main class used to tune and train Keras models for text classification using Array data.
    """


    def __init__(self, model, train_data=None, val_data=None, 
                 batch_size=U.DEFAULT_BS, workers=1, use_multiprocessing=False, multigpu=False):
        super().__init__(model, train_data=train_data, val_data=val_data,
                         batch_size=batch_size, 
                         workers=workers, use_multiprocessing=use_multiprocessing,
                         multigpu=multigpu)
        return


    def view_top_losses(self, n=4, preproc=None, val_data=None):
        """
        Views observations with top losses in validation set.
        Args:
         n(int or tuple): a range to select in form of int or tuple
                          e.g., n=8 is treated as n=(0,8)
         preproc (Preprocessor): A TextPreprocessor or ImagePreprocessor.
                                 For some data like text data, a preprocessor
                                 is required to undo the pre-processing
                                 to correctly view raw data.
          val_data:  optional val_data to use instead of self.val_data
        Returns:
            list of n tuples where first element is either 
            filepath or id of validation example and second element
            is loss.

        """
        val = self._check_val(val_data)


        # get top losses and associated data
        tups = self.top_losses(n=n, val_data=val, preproc=preproc)

        # get multilabel status and class names
        classes = preproc.get_classes() if preproc is not None else None

        # iterate through losses
        for tup in tups:

            # get data
            idx = tup[0]
            loss = tup[1]
            truth = tup[2]
            pred = tup[3]

            # BERT-style tuple
            join_char = ' '
            obs = val[0][0][idx]
            if preproc is not None: 
                obs = preproc.undo(obs)
                if preproc.is_nospace_lang(): join_char = ''
            if type(obs) == str:
                obs = join_char.join(obs.split()[:512])
            print('----------')
            print("id:%s | loss:%s | true:%s | pred:%s)\n" % (idx, round(loss,2), truth, pred))
            print(obs)
        return
