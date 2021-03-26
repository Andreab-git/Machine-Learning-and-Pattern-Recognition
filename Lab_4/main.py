import numpy as np
import matplotlib.pyplot as plt


def GAU_pdf(x, mu, var):
    # Compute normal probability density function
    return (1 / np.sqrt(2 * np.pi * var)) * np.exp(- ((x - mu) ** 2) / (2 * var))


def GAU_logpdf(x, mu, var):
    return (-0.5 * np.log(2 * np.pi)) - 0.5 * np.log(var) - ((x - mu) ** 2 / (2 * var))


def log_likelihood(x, mu, var):
    return GAU_logpdf(x, mu, var).sum()


def logpdf_GAU_ND(x, mu, C):
    # M is the size of the feature vector x
    M = x.shape[0]
    inv = np.linalg.inv(C)
    val, abs_log_det = np.linalg.slogdet(C)
    print(abs_log_det)
    return -0.5 * M * np.log(2 * np.pi) - 0.5 * abs_log_det - 0.5 * ((x - mu).T.dot(inv).dot(x - mu)).sum(axis=1)


if __name__ == '__main__':
    XGAU = np.load('Data/XGau.npy')
    CND = np.load('Solution/CND.npy')
    XND = np.load('Solution/XND.npy')
    muND = np.load('Solution/muND.npy')

    plt.hist(XGAU, bins=50, density=True)

    # Checking density with the solutions
    XPlot = np.linspace(-8, 12, 1000)
    pdfSol = np.load('Solution/CheckGAUPdf.npy')
    pdfGau = GAU_pdf(XPlot, 1.0, 2.0)
    # The result should be zero or very close to zero
    # print(np.abs(pdfSol - pdfGau).mean())

    # Trying to compute the likelihood for our dataset XGAU
    ll_samples = GAU_pdf(XGAU, 1.0, 2.0)
    likelihood = ll_samples.prod()
    # print(likelihood)

    # Gaussian ML estimate
    m_ML = XGAU.mean()
    v_ML = XGAU.var()
    ll = log_likelihood(XGAU, m_ML, v_ML)
    # print(ll)

    plt.plot(XPlot, np.exp(GAU_logpdf(XPlot, m_ML, v_ML)))
    plt.show()

    # Multivariate Gaussian
    print(logpdf_GAU_ND(XND, muND, CND))
