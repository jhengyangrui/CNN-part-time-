install.packages("stringr")
install.packages("xlsx")
library(stringr)
library(xlsx)

files <- list.files(path = "./", pattern = "*.txt")

result_m = matrix(NA, ncol = 5, nrow = 0)
colnames(result_m) = c("檔案名稱", "第一類", "第二類", "第三類", "第四類")

tt_all = as.character(NULL)
for(i in 1:length(files)){
  tt = readLines(files[[i]], encoding = "UTF-8")
  
  for(j in 1:length(tt)){
    tt_all = paste(tt_all, tt[j])
  }
  
  tt_split = strsplit(tt_all, split = "。")
  
  temp_m = matrix(NA, ncol = 5, nrow = 1)
  
  key_f = as.vector(NULL)
  key_f = c(key_f, "加速", "加快", "促進")
  key_f = c(key_f, "目標", "目的", "宗旨", "意圖", "意向")
  key_f = c(key_f, "預知", "預料", "意圖", "意想")
  key_f = c(key_f, "期待", "期盼", "意料")
  key_f = c(key_f, "相信", "認為", "以為", "想得到")
  key_f = c(key_f, "可以", "能夠", "會")
  key_f = c(key_f, "能", "可以")
  key_f = c(key_f, "未來", "就要來的", "正式來的", "來年", "次日", "次年", "下月", "下週", "下一年", "有前途的", "正在崛起的", "蒸蒸日上的")
  key_f = c(key_f, "接下來的年度", "接下來的財務年度")
  key_f = c(key_f, "接下來的月份")
  key_f = c(key_f, "自信")
  key_f = c(key_f, "說服", "使信服")
  key_f = c(key_f, "當年度", "當前年度", "當前財務年度")
  key_f = c(key_f, "設想", "預知", "預料","想得到")
  key_f = c(key_f, "估計", "預算", "臆測", "估量")
  key_f = c(key_f, "最終")
  key_f = c(key_f, "期望", "期待", "預期", "預料")
  key_f = c(key_f, "之後", "以後", "隨後")
  key_f = c(key_f, "預測", "預報", "展望")
  key_f = c(key_f, "即將到來")
  key_f = c(key_f, "未來", "將來", "將來的事", "前途", "前景", "前程")
  key_f = c(key_f, "目標", "目的", "意圖")
  key_f = c(key_f, "希望", "期望", "期許", "冀望")
  key_f = c(key_f, "進來的", "即將就任的")
  key_f = c(key_f, "意圖", "打算", "準備")
  key_f = c(key_f, "可能", "容易", "或許", "不會", "不太可能")
  key_f = c(key_f, "展望", "意料", "向前看", "期待")
  key_f = c(key_f, "下一個", "未來", "下一次", "然後")
  key_f = c(key_f, "新興", "新奇")
  key_f = c(key_f, "可能", "可以")
  key_f = c(key_f, "可能", "可以", "可能性", "也許", "允許")
  key_f = c(key_f, "目標", "目的", "意圖", "意向")
  key_f = c(key_f, "開朗的", "樂觀的")
  key_f = c(key_f, "前景", "展望", "遠景")
  key_f = c(key_f, "計畫")
  key_f = c(key_f, "預測", "預計", "意料")
  key_f = c(key_f, "預測", "估計", "預計", "計畫", "規劃")
  key_f = c(key_f, "前景", "展望", "遠景", "前途")
  key_f = c(key_f, "殘留", "有待")
  key_f = c(key_f, "更新", "恢復", "續借")
  key_f = c(key_f, "尋找", "尋求")
  key_f = c(key_f, "適用範圍", "規模")
  key_f = c(key_f, "將", "將要")
  key_f = c(key_f, "不久", "立刻")
  key_f = c(key_f, "應該", "應", "應當", "理應")
  key_f = c(key_f, "不久", "早日", "在即", "最近")
  key_f = c(key_f, "隨後的", "後來的")
  key_f = c(key_f, "未必的", "不一定有把握的", "不太可能的", "不可能發生的")
  key_f = c(key_f, "即將來到的", "即將出現的", "即將到來", "即將來臨的", "預定將要")
  key_f = c(key_f, "將", "將會", "將要")
  key_f = c(key_f, "好地方", "好的位置", "位置優越")
  key_f = c(key_f, "年前")
  
  key_profit = as.vector(NULL)
  key_profit = c(key_profit, "EPS", "每股盈餘", "收益", "損失", "虧損", "減少", "利潤", "盈利")
  
  key_amount = as.vector(NULL)
  key_amount = c(key_amount, "元", "千元", "百萬元", "$", "%", "百分之", "成")
  
  count_1 = 0
  for(i in 1:length(tt_split[[1]])){
    if(sum(str_count(tt_split[[1]][i], key_f)) > 0){
      count_1 = count_1 + 1
    }
  }
  
  count_2 = 0
  for(i in 1:length(tt_split[[1]])){
    if(sum(str_count(tt_split[[1]][i], key_f)) > 0 & sum(str_count(tt_split[[1]][i], key_profit)) > 0){
      count_2 = count_2 + 1
    }
  }
  
  count_3 = 0
  for(i in 1:length(tt_split[[1]])){
    if(sum(str_count(tt_split[[1]][i], key_f)) > 0 & sum(str_count(tt_split[[1]][i], key_amount)) > 0){
      count_3 = count_3 + 1
    }
  }
  
  count_4 = 0
  for(i in 1:length(tt_split[[1]])){
    if(sum(str_count(tt_split[[1]][i], key_f)) > 0 & sum(str_count(tt_split[[1]][i], key_amount)) > 0 & sum(str_count(tt_split[[1]][i], key_profit)) > 0){
      count_4 = count_4 + 1
    }
  }
  
  #write.xlsx(m1_score, "demo_1.xlsx")
  #write.xlsx(m2_score, "demo_2.xlsx")
  
  # print("\f", "第一類：", count_1, "\n",
  #     "第二類：", count_2, "\n",
  #     "第三類：", count_3, "\n",
  #     "第四類：", count_4)
  
  temp_m[1,1] = files[[1]]  
  temp_m[1,2] = count_1
  temp_m[1,3] = count_2
  temp_m[1,4] = count_3
  temp_m[1,5] = count_4
  
  result_m = rbind(result_m, temp_m)
}