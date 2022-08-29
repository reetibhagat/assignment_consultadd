temps <- read.delim(file.choose())
head(temps)

# 1996 data
data <- temps$X1996
data
date_avgs <- rowMeans(temps[c(2:length(temps))], dims = 1, na.rm = T)
da_mu <- mean(date_avgs)
da_minus_mu <- date_avgs - da_mu
C <- 4
damimu_minus_C <- da_minus_mu - C
precusum <- 0 * damimu_minus_C
cusum <- append(precusum, 0)
for (i in 1:length(damimu_minus_C))
{
  checker <- cusum[i] + damimu_minus_C[i]

  ifelse(checker > 0, cusum[i + 1] <- checker, cusum[i + 1] <- 0)
}

cusum
plot(cusum)
which(cusum >= 85)
temps[56, 1]
