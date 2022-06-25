rm(list=ls())
library(pheatmap)
#data <- read.delim("C:/Users/Administrator/Desktop/biomass_covid/gamma.csv",sep=",",header = FALSE)
data<-read.csv("C:/Users/Administrator/Desktop/biomass_covid/zujian.csv")
rownames(data)<-data[,1]
data=data[,-1]
data=t(data)
expdata <- as.matrix(data)
pheatmap(expdata,cluster_cols = FALSE,cluster_row=FALSE
         ,main = "Heatmap of abs diffrence between virants"
         ,filename = "C:/Users/Administrator/Desktop/biomass_covid/zujian_juedui.png")

data<-read.csv("C:/Users/Administrator/Desktop/biomass_covid/alpha.csv")
rownames(data)<-data[,1]
data=data[,-1]
data=t(data)
expdata <- as.matrix(data)
pheatmap(expdata,cluster_cols = FALSE,cluster_row=FALSE
         ,main = "Heatmap of diffrence between alpha virants"
         ,filename = "C:/Users/Administrator/Desktop/biomass_covid/alpha.png")

data<-read.csv("C:/Users/Administrator/Desktop/biomass_covid/beta.csv")
rownames(data)<-data[,1]
data=data[,-1]
data=t(data)
expdata <- as.matrix(data)
pheatmap(expdata,cluster_cols = FALSE,cluster_row=FALSE
         ,main = "Heatmap of diffrence between beta virants"
         ,filename = "C:/Users/Administrator/Desktop/biomass_covid/beta.png")

data<-read.csv("C:/Users/Administrator/Desktop/biomass_covid/gamma.csv")
rownames(data)<-data[,1]
data=data[,-1]
data=t(data)
expdata <- as.matrix(data)
pheatmap(expdata,cluster_cols = FALSE,cluster_row=FALSE
         ,main = "Heatmap of diffrence between gamma virants"
         ,filename = "C:/Users/Administrator/Desktop/biomass_covid/gamma.png")

data<-read.csv("C:/Users/Administrator/Desktop/biomass_covid/epsilon.csv")
rownames(data)<-data[,1]
data=data[,-1]
data=t(data)
expdata <- as.matrix(data)
pheatmap(expdata,cluster_cols = FALSE,cluster_row=FALSE
         ,main = "Heatmap of diffrence between epsilon virants"
         ,filename = "C:/Users/Administrator/Desktop/biomass_covid/epsilon.png")


