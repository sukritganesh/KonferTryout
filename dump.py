def isEnoughData(self,df,columns):
        '''
        Args:
            df -> input dataframe
            columns -> target feature name(list)
        Returns:
            It return True/False based on distinct value count of the target feature
        '''
        print('your move')
        for col in columns:
            distcnt = np.count_nonzero(df[col], axis=0)
            if (distcnt < 10):
                return False
            # sd = df[col].std()
        return True

    