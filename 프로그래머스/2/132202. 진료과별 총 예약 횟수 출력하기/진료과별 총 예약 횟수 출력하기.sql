SELECT MCDP_CD AS "진료과코드", COUNT(*) AS "5월예약건수"
FROM APPOINTMENT
WHERE APNT_YMD LIKE "2022-05-%"
GROUP BY MCDP_CD
ORDER BY `5월예약건수` ASC, MCDP_CD ASC;


-- Line 5의 정렬 기준을 "5월예약건수" 로 설정하여 틀림
-- backtick(``)을 사용하면 literal이 아닌 이름 그 자체로 인식됨을 알게 됨