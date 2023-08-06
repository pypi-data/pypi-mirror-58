class nmr_classifier(BaseEstimator, RegressorMixin):
    """ Classifier using NMR
    
    Parameters
    ----------
    A : array, shape=[n_samples, horizontal pixels, vertical pixels]
    
    B : array, shape=[horizontal pixels, vertical pixels]
    
    x : array, shape=[n_samples]
        Representation of regression coefficient vector for each image.
    
    lambd : float, deault=1.0
    mu : float, deault=1.0
    gamma : float, deault=1.0
    ep_abs : float, deault=1.0
    ep_rel : float, deault=1.0 
    max_iter : float, deault=10
    
     Attributes
    ----------
    x_new : array, shape=[n_samples]
    Representation of the optimal regression coefficient vector for each image.
    
     Examples
    --------
    >>> from nmr_classifier.fast_admm_nmr import fast_admm_nmr
    >>> 
    
    """
    
    def __init__(self, lambd=1.0, mu=1.0, gamma=1.0, ep_abs=0.01, ep_rel=0.01, max_iter=100):
        self.lambd = lambd
        self.mu = mu
        self.gamma = gamma
        
        self.ep_abs = ep_abs
        self.ep_rel = ep_rel
        self.max_iter = max_iter
        
    
    
    def coef_img(self,A,x):
        A_x = np.zeros((A.shape[1], A.shape[2]))
        n = A.shape[0]
        for num in range(n):
            A_x += x[num]*A[num]
        return A_x
    
    
    
    def vec(self,input_array):
        return input_array.T.reshape(-1,1).T.tolist()[0]
    
    
    
    def svt(self, A_x, B, Z):
        svt_in = A_x - B + 1/self.mu*Z
        U, S, V = np.linalg.svd(svt_in, full_matrices=False)
        S = np.maximum(S - 1/self.mu, 0)
        Y = np.linalg.multi_dot([U, np.diag(S), V])
        return Y
    
    
    
    def fit(self, A, B):
        
        n = A.shape[0]
        p = A.shape[1]
        q = A.shape[2]
        
        # Step 1
        H_T = np.zeros((p*q, n)).T
        for n_iter in range(n) :
            H_T[n_iter] = self.vec(A[n_iter])
        H = H_T.T
        theta = self.lambd*(1+self.gamma)
        M = np.dot(np.linalg.inv(np.dot(H.T,H)+theta/self.mu*np.identity(H.shape[1])), H.T)
        
        
        # Step 2
        x = np.zeros(n)
        xhat = np.zeros(n)
        Z = 0
        Zhat = 0
        Y = 0
        alpha = 1
        k = 0
        
        # Step 3 ~ 5
        for iter_loop in range(self.max_iter):

            # Updating Y
            A_xhat = self.coef_img(A,xhat)
            Y_new = self.svt(A_xhat, B, Z)
            
            
            # Updating x
            g_in = B + Y_new - 1/self.mu*Zhat
            g = self.vec(g_in)
            x_new = np.dot(M, g)

            
            # Updating Z
            A_x_new = self.coef_img(A,x_new)
            Z_new = Zhat + self.mu*(A_x_new - Y_new - B)
            
            
            # Updating alpha
            alpha_new = (1+np.sqrt(1+4*alpha*alpha))/2
            
            
            # Updating xhat
            xhat_new = x + (alpha-1)/alpha_new*(x_new-x)
            
            
            # Updating Zhat
            Zhat_new = Z + (alpha-1)/alpha_new*(Z_new-Z)
            

            # termination 
            r_pri = A_x_new - Y_new - B
            ep_pri = np.sqrt(p*q)*self.ep_abs + self.ep_rel*max(np.linalg.norm(A_x_new,ord='nuc'),np.linalg.norm(Y_new,ord='nuc'),np.linalg.norm(B,ord='nuc'))
            s_dual = 1/self.mu * np.dot(H.T, self.vec(Y-Y_new))
            ep_dual = np.sqrt(n)*self.ep_abs + self.ep_rel*np.linalg.norm(np.dot(H.T, Z_new.T.reshape(-1,1).T.tolist()[0]),ord=2)


            if(np.linalg.norm(r_pri, ord=2)<=ep_pri and np.linalg.norm(s_dual, ord=2)<=ep_dual):
                 break    # break here


            x = x_new
            xhat = xhat_new
            Y = Y_new
            Z = Z_new
            Zhat = Zhat_new

        
        return x
    
    
    
    
    def classifier(self, A, B, target):
        x = self.fit(A,B)
        A_x = self.coef_img(A,x)
        
        # A_x_i + error
        target_unique = np.unique(target)
        error_lst = []
        for i in target_unique:
            target_tf = (target == target_unique[i])
            x_i = x[target_tf]
            A_i = A[target_tf,:,:]
            A_x_i = self.coef_img(A_i,x_i)
            
            diff = A_x - A_x_i
            error = np.linalg.norm(diff,ord='nuc')
            error_lst.append(error)
            
        error = np.array(error_lst)
        error_tf = (error==min(error))
        val = target_unique[error_tf]
        
        # Return smallest error label
        return val[0]


    
    
    def classifier_top(self, A, B, target, top_num):
        x = self.fit(A,B)
        A_x = self.coef_img(A,x)
        
        # A_x_i + error
        target_unique = np.unique(target)
        error_lst = []
        for i in target_unique:
            target_tf = (target == target_unique[i])
            x_i = x[target_tf]
            A_i = A[target_tf,:,:]
            A_x_i = self.coef_img(A_i,x_i)
            
            diff = A_x - A_x_i
            error = np.linalg.norm(diff,ord='nuc')
            error_lst.append(error)
            
        error = np.array(error_lst)
        
        # top-n error
        error_top = np.sort(error)[:top_num] 
        error_top_tf = [val in error_top for val in error]
        val_top = target_unique[error_top_tf]
        
        # Matching Labels with Results
        error_min_tf = (error==min(error)) 
        val_min = target_unique[error_min_tf]
        
        # Return (smallest error label, top-n error label)
        return val_min[0], val_top
    