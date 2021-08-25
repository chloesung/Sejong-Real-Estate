# Sejong Real Estate

<img width="1212" alt="스크린샷 2021-08-25 오후 3 22 13" src="https://user-images.githubusercontent.com/71932401/130737257-34157fce-c1a6-4faf-a2a2-f05caea6431c.png">

## LH COMPAS 세종시 주택시장 특성 분석 공모전 최우수상 수상 (1등)
- **주최**: LH 한국도시주택공사
- **분석 목적**: 본 과제는 과거 4개년도의 부동산 실거래정보와 전입‧전출 등 거주인구 정보, 상권정보 및 건물 등 공간데이터를 활용, 세종시 주택 시장 특성을 직관적으로 이해 할 수 있는 다양한 모델을 도출하는데 목적이 있습니다.
- **해결 과제**: 세종시 주택 시장 특성을 쉽고 명확히 보이도록 시각화 모델 제시
- **웹페이지**: [COMPAS 세종시 주택시장 특성 분석](https://compas.lh.or.kr/noticeinfo?pageIndex=1&pageSize=10&searchKey=both&searchText=&totalCount=55&brdArtclNo=1282)

## Introduction
2012년 새롭게 출범한 세종특별자치시는, **'행정중심복합도시'** 라는 우리나라에서 처음으로 시도하는 특별한 형태의 도시입니다. 또한 작년, '세종천도설' 등 여러 이슈에 휩싸이며 주택의 거래량이 가장 빠르게 증가하던 곳이기도 합니다. 그래서 저희는 데이터를 통해 **세종시의 주택시장이 어떤 특징을 가지고 있는지**를 중심으로 명료한 시각화 모델을 통해 제시하고자 합니다.   

## Team 세종대왕
성유지, 오세린, 윤정현, 이나윤, 이영신   
💬 Contact: chloesung@korea.ac.kr

## 구조
1. **Data Preprocessing:** 500x500 격자 생성 후 그리드 별로 데이터 전처리
2. **Visualiztion:** 시기 별 뉴스 데이터 시각화 및 수치 데이터 지도에 시각화
3. **Modeling:** 그리드 별 지수 생성, 뉴스 데이터 LDA, 다중회귀분석 및 Oaxaca Decomposition
4. **Crawling:** 네이버 뉴스, 카카오맵 크롤링
5. **Slides:** 최종 발표 슬라이드 및 시각화 분석 

## Visualization
### 시기 별 이슈 확인 (WordCloud)
![세종대왕_시각화분석결과물-02](https://user-images.githubusercontent.com/71932401/130740019-2cfec62a-af88-4e44-adba-de4c28a7733e.png)

### 주택 및 거래 관련
![세종대왕_시각화분석결과물-03](https://user-images.githubusercontent.com/71932401/130740138-9b7a33a5-685d-4a51-8adb-fab4eacd36a5.png)
![세종대왕_시각화분석결과물-04](https://user-images.githubusercontent.com/71932401/130740147-768a5483-68f1-4870-bd39-99f40f83a264.png)

### 인구 관련
![세종대왕_시각화분석결과물-05](https://user-images.githubusercontent.com/71932401/130740216-d61db4d3-2b7c-4a4f-b592-2ce21fb5e549.png)
![세종대왕_시각화분석결과물-06](https://user-images.githubusercontent.com/71932401/130740245-a7dd3b0e-1463-4e25-96ea-6e92f1c3c438.png)

## Modeling
### 지수 생성 및 LDA
![세종대왕_시각화분석결과물-07](https://user-images.githubusercontent.com/71932401/130741182-20cf09a5-6d0d-49c4-95b8-2ccff48a1f05.png)

### Multiple Regression Analysis 및 Oaxaca Decomposition
![세종대왕_시각화분석결과물-08](https://user-images.githubusercontent.com/71932401/130741194-44127f43-0603-4acb-861c-3896b8f980e4.png)

## 결과 요약 및 제언
![세종대왕_시각화분석결과물-09](https://user-images.githubusercontent.com/71932401/130741310-b8651d99-0f04-40d8-8bd7-72433e677bcc.png)
![세종대왕_시각화분석결과물-10](https://user-images.githubusercontent.com/71932401/130741326-1580ce14-4467-43bd-89c9-0146b1694515.png)
![세종대왕_시각화분석결과물-11](https://user-images.githubusercontent.com/71932401/130741336-f6924fb8-5f8a-4ee9-b9c3-19be1f92c8dc.png)
![세종대왕_시각화분석결과물-12](https://user-images.githubusercontent.com/71932401/130741341-bd66cc2e-2ed9-4b40-bd8c-a90c9d6276b0.png)
