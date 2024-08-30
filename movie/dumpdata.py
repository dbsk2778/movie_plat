# -*- conding: utf-8 -*-

import json
import requests

result_genres = [
    {
      "id": 28,
      "name": "액션"
    },
    {
      "id": 12,
      "name": "모험"
    },
    {
      "id": 16,
      "name": "애니메이션"
    },
    {
      "id": 35,
      "name": "코미디"
    },
    {
      "id": 80,
      "name": "범죄"
    },
    {
      "id": 99,
      "name": "다큐멘터리"
    },
    {
      "id": 18,
      "name": "드라마"
    },
    {
      "id": 10751,
      "name": "가족"
    },
    {
      "id": 14,
      "name": "판타지"
    },
    {
      "id": 36,
      "name": "역사"
    },
    {
      "id": 27,
      "name": "공포"
    },
    {
      "id": 10402,
      "name": "음악"
    },
    {
      "id": 9648,
      "name": "미스터리"
    },
    {
      "id": 10749,
      "name": "로맨스"
    },
    {
      "id": 878,
      "name": "SF"
    },
    {
      "id": 10770,
      "name": "TV 영화"
    },
    {
      "id": 53,
      "name": "스릴러"
    },
    {
      "id": 10752,
      "name": "전쟁"
    },
    {
      "id": 37,
      "name": "서부"
    }
]

result = [
    
    {
      "popularity": 1307.787,
      "vote_count": 209,
      "video": "False",
      "poster_path": "/hSpm2mMbkd0hLTRWBz0zolnLAyK.jpg",
      "id": 671039,
      "adult": "False",
      "backdrop_path": "/gnf4Cb2rms69QbCnGFJyqwBWsxv.jpg",
      "original_language": "fr",
      "original_title": "Bronx",
      "genre_ids": [
        53,
        28,
        18,
        80
      ],
      "title": "로그 시티",
      "vote_average": 6,
      "overview": "부패경찰과 마르세유의 조폭 사이의 문제로 위기의  경찰조직을 보호해야 한다.",
      "release_date": "2020-10-30"
    },
    {
      "popularity": 1232.799,
      "vote_count": 1416,
      "video": "False",
      "poster_path": "/jcJpkQWRU8gsZlo830eQ8ryXKNU.jpg",
      "id": 400160,
      "adult": "False",
      "backdrop_path": "/wu1uilmhM4TdluKi2ytfz8gidHf.jpg",
      "original_language": "en",
      "original_title": "The SpongeBob Movie: Sponge on the Run",
      "genre_ids": [
        14,
        16,
        12,
        35,
        10751
      ],
      "title": "스폰지밥 무비: 핑핑이 구출 대작전",
      "vote_average": 8.1,
      "overview": "우리 핑핑이가 어디로 갔을까? 설마, 납치당한 건가? 사랑하는 반려 달팽이를 찾아 떠나는 스폰지밥. 뚱이도 함께 가야지. 비키니 시티를 벗어나 미지의 세계로, 출발이다!",
      "release_date": "2020-08-14"
    },
    {
      "popularity": 1387.546,
      "vote_count": 338,
      "video": "False",
      "poster_path": "/7D430eqZj8y3oVkLFfsWXGRcpEG.jpg",
      "id": 528085,
      "adult": "False",
      "backdrop_path": "/5UkzNSOK561c2QRy2Zr4AkADzLT.jpg",
      "original_language": "en",
      "original_title": "2067",
      "genre_ids": [
        878,
        53,
        18
      ],
      "title": "2067",
      "vote_average": 4.7,
      "overview": "",
      "release_date": "2020-10-01"
    },
    {
      "popularity": 1259.974,
      "id": 724989,
      "video": "False",
      "vote_count": 152,
      "vote_average": 5,
      "title": "하드 킬",
      "release_date": "2020-10-23",
      "original_language": "en",
      "original_title": "Hard Kill",
      "genre_ids": [
        28,
        53
      ],
      "backdrop_path": "/86L8wqGMDbwURPni2t7FQ0nDjsH.jpg",
      "adult": "False",
      "overview": "",
      "poster_path": "/ugZW8ocsrfgI95pnQ7wrmKDxIe.jpg"
    },
    {
      "popularity": 964.599,
      "vote_count": 720,
      "video": "False",
      "poster_path": "/betExZlgK0l7CZ9CsCBVcwO1OjL.jpg",
      "id": 531219,
      "adult": "False",
      "backdrop_path": "/8rIoyM6zYXJNjzGseT3MRusMPWl.jpg",
      "original_language": "en",
      "original_title": "Roald Dahl's The Witches",
      "genre_ids": [
        14,
        10751,
        12,
        35,
        27
      ],
      "title": "마녀를 잡아라",
      "vote_average": 6.9,
      "overview": "마녀들로부터 발각되어 생쥐로 변해버린 소년이 과거 마녀전담반이었던 할머니와 함께 마녀들과 맞선다는 내용의 판타지 어드벤처",
      "release_date": "2020-10-26"
    },
    {
      "popularity": 859.937,
      "vote_count": 158,
      "video": "False",
      "poster_path": "/elZ6JCzSEvFOq4gNjNeZsnRFsvj.jpg",
      "id": 741067,
      "adult": "False",
      "backdrop_path": "/mc48QVtMhohMFrHGca8OHTB6C2B.jpg",
      "original_language": "en",
      "original_title": "Welcome to Sudden Death",
      "genre_ids": [
        28,
        53,
        12,
        18
      ],
      "title": "웰컴 투 서든 데쓰",
      "vote_average": 6.4,
      "overview": "",
      "release_date": "2020-09-29"
    },
    {
      "popularity": 745.918,
      "vote_count": 2630,
      "video": "False",
      "poster_path": "/riYInlsq2kf1AWoGm80JQW5dLKp.jpg",
      "id": 497582,
      "adult": "False",
      "backdrop_path": "/kMe4TKMDNXTKptQPAdOF0oZHq3V.jpg",
      "original_language": "en",
      "original_title": "Enola Holmes",
      "genre_ids": [
        80,
        18,
        9648
      ],
      "title": "에놀라 홈즈",
      "vote_average": 7.5,
      "overview": "열여섯 생일을 맞은 셜록의 여동생, 에놀라 홈즈. 사라진 엄마를 찾아 런던으로 향한다. 명석한 두뇌의 대명사인 오빠까지 따돌리고, 위험에 빠진 귀족 청년의 미스터리와 엮이는데. 사건을 추적하며, 홈즈 가문답게 예리한 추리력이 폭발한다. 미스터리 가득한 이 모험, 무사히 마칠 수 있을까?",
      "release_date": "2020-09-23"
    },
    {
      "popularity": 681.098,
      "vote_count": 735,
      "video": "False",
      "poster_path": "/bqZRy3tJjJIrA38FSdqJEufQ2Os.jpg",
      "id": 340102,
      "adult": "False",
      "backdrop_path": "/eCIvqa3QVCx6H09bdeOS8Al2Sqy.jpg",
      "original_language": "en",
      "original_title": "The New Mutants",
      "genre_ids": [
        28,
        878,
        27,
        12
      ],
      "title": "뉴 뮤턴트",
      "vote_average": 6.3,
      "overview": "십대의 돌연변이 레인과 일리, 샘, 로베르토는 비밀 시설에 수용되어 심리 상태를 감시 받는다. 이들이 사회에는 물론 스스로에게도 위험한 존재라고 생각하는 닥터 레예스는 이들에게 돌연변이 능력을 통제하는 방법을 가르쳐주고자 애쓴다. 어느 날, 대재앙이 덮친 마을에서 혼자 살아남은 대니가 이곳에 들어오며 끔찍한 일들이 벌어지기 시작하고, 자신들의 힘을 두려워하고 다룰 줄 몰랐던 십대 돌연변이들은 믿기지 않는 경험을 하며 자신들의 능력을 각성하기 시작하는데…",
      "release_date": "2020-08-26"
    },
    {
      "popularity": 697.979,
      "vote_count": 154,
      "video": "False",
      "poster_path": "/zfdhsR3Y3xw42OHrMpi0oBw0Uk8.jpg",
      "id": 741074,
      "adult": "False",
      "backdrop_path": "/DA7gzvlBoxMNL0XmGgTZOyv67P.jpg",
      "original_language": "en",
      "original_title": "Once Upon a Snowman",
      "genre_ids": [
        16,
        10751,
        35,
        14
      ],
      "title": "원스 어폰 어 스노우맨",
      "vote_average": 7,
      "overview": "",
      "release_date": "2020-10-23"
    },
    {
      "popularity": 731.692,
      "id": 337401,
      "video": "False",
      "vote_count": 2922,
      "vote_average": 7.2,
      "title": "뮬란",
      "release_date": "2020-09-04",
      "original_language": "en",
      "original_title": "Mulan",
      "genre_ids": [
        28,
        12,
        18,
        14
      ],
      "backdrop_path": "/zzWGRw277MNoCs3zhyG3YmYQsXv.jpg",
      "adult": "False",
      "overview": "무예에 남다른 재능을 지닌 뮬란은 좋은 집안과 인연을 맺어 가문을 빛내길 바라는 부모님의 뜻에 따라 본연의 모습을 억누르고 성장한다. 어느 날, 북쪽 오랑캐들이 침입하자 황제는 징집령을 내리고 뮬란은 아픈 아버지를 대신해 가족들 몰래 전장에 나가기로 결심한다. 여자라는 게 발각되면 목숨을 잃을 수도 있는 상황 속에서 뮬란은 타고난 용기와 지혜로 역경을 이겨내며 전사로 성장한다. 마침내 잔인무도한 적장 보리 칸과 마녀 시아니앙을 마주하게 된 뮬란. 그녀는 위험에 빠진 동료와 가족을 구하고 진정한 전사로 거듭날 수 있을 것인가?",
      "poster_path": "/mQbxBKeRuAofS5p2w4mK7DqtS97.jpg"
    },
    {
      "popularity": 588.401,
      "id": 571384,
      "video": "False",
      "vote_count": 42,
      "vote_average": 6.5,
      "title": "컴 플레이",
      "release_date": "2020-10-28",
      "original_language": "en",
      "original_title": "Come Play",
      "genre_ids": [
        27
      ],
      "backdrop_path": "/5HahZPsGGaDgnFb68J49ZwdwU0b.jpg",
      "adult": "False",
      "overview": "",
      "poster_path": "/e98dJUitAoKLwmzjQ0Yxp1VQrnU.jpg"
    },
    {
      "popularity": 544.621,
      "vote_count": 71,
      "video": "False",
      "poster_path": "/m2FNRngyJMyxLatBMJR8pbeG2v.jpg",
      "id": 635302,
      "adult": "False",
      "backdrop_path": "/d1sVANghKKMZNvqjW0V6y1ejvV9.jpg",
      "original_language": "ja",
      "original_title": "劇場版「鬼滅の刃」無限列車編",
      "genre_ids": [
        16,
        28,
        36,
        12,
        14,
        18
      ],
      "title": "극장판 귀멸의 칼날: 무한열차편",
      "vote_average": 6.2,
      "overview": "혈귀로 변해버린 여동생 ‘네즈코’를 인간으로 되돌릴 단서를 찾아 비밀조직 귀살대에 들어간 ‘탄지로.’ ‘젠이츠’, ‘이노스케’와 새로운 임무 수행을 위해 무한열차에 탑승 후 귀살대 최강 검사 염주 ‘렌고쿠’와 합류한다. 달리는 무한열차에서 승객들이 하나 둘 흔적 없이 사라지자 숨어있는 식인 혈귀의 존재를 직감하는 ‘렌고쿠’. 귀살대 ‘탄지로’ 일행과 최강 검사 염주 ‘렌고쿠’는 어둠 속을 달리는 무한열차에서 모두의 목숨을 구하기 위해 예측불가능한 능력을 가진 혈귀와 목숨을 건 혈전을 시작하는데…",
      "release_date": "2020-10-16"
    },
    {
      "popularity": 546.597,
      "vote_count": 427,
      "video": "False",
      "poster_path": "/zG6QJjd5feBZBl7zeKHDDlgL8FY.jpg",
      "id": 560050,
      "adult": "False",
      "backdrop_path": "/htBUhLSS7FfHtydgYxUWjL3J1Q1.jpg",
      "original_language": "en",
      "original_title": "Over the Moon",
      "genre_ids": [
        16,
        12,
        10751,
        14
      ],
      "title": "오버 더 문",
      "vote_average": 7.7,
      "overview": "믿는 사람에게만 펼쳐지는 세상 똑똑하고 호기심 넘치는 소녀 페이 페이, 엄마가 어린 시절 들려준 전설 속 달의 여신 항아 이야기를 늘 마음에 풀고 살아간다. 일찍 하늘나라로 간 엄마를 그리워하며 살아가던 페이 페이는 어느 날 항아의 전설이 지어낸 이야기일 뿐이라는 고모의 말에 울컥해, 항아의 존재를 증명하기 위해 달로 향하는 로켓을 만들기로 결심한다. 수많은 시행착오 끝에 로켓 만들기에 성공한 페이 페이, 예상치 못한 모험을 떠나게 된 소녀는 신기한 생명체로 가득한 기묘한 세계를 발견하게 되는데…",
      "release_date": "2020-10-16"
    },
    {
      "popularity": 536.503,
      "vote_count": 67,
      "video": "False",
      "poster_path": "/k8Q9ulyRE8fkvZMkAM9LPYMKctb.jpg",
      "id": 618353,
      "adult": "False",
      "backdrop_path": "/kU7ZiyeUwcpTkYj3UcxSqGdZmxY.jpg",
      "original_language": "en",
      "original_title": "Batman: Death in the Family",
      "genre_ids": [
        16,
        28
      ],
      "title": "배트맨: 데스 인 더 패밀리",
      "vote_average": 7.8,
      "overview": "",
      "release_date": "2020-10-13"
    },
    {
      "popularity": 528.93,
      "vote_count": 12,
      "video": "False",
      "poster_path": "/AnVD7Gn14uOTQhcc5xYZGQ9DRvS.jpg",
      "id": 624779,
      "adult": "False",
      "backdrop_path": "/h5sUE9jqoYrjsFjANJXL0gpZGye.jpg",
      "original_language": "en",
      "original_title": "VFW",
      "genre_ids": [
        28,
        53,
        27
      ],
      "title": "브이에프더블유",
      "vote_average": 4.9,
      "overview": "옛 전우들이 모여 술을 마시고 대화를 나누는 VFW(해외참전용사) 모임이 있던 밤. 어린 소녀 하나가 훔친 마약을 들고 그 모임에 들이닥친다. 그 뒤를 이어 잔인한 폭력배들이 여자 아이를 추적하면서 그 모임은 소녀와 퇴역군인 모두를 위한 생존 오두막으로 바뀐다. 참전용사들은 마약에 찌든 폭력배들의 끊임없는 공격에 총력전을 펼치기 위해 모을 수 있는 무기를 전부 모아 들이고, 결국 전면전이 뒤따른다.",
      "release_date": "2020-10-14"
    },
    {
      "popularity": 544.473,
      "vote_count": 635,
      "video": "False",
      "poster_path": "/fJ0i5MKbBTKJGYY2uxsiUMdwMc6.jpg",
      "id": 539885,
      "adult": "False",
      "backdrop_path": "/54yOImQgj8i85u9hxxnaIQBRUuo.jpg",
      "original_language": "en",
      "original_title": "Ava",
      "genre_ids": [
        28,
        80,
        18,
        53
      ],
      "title": "에이바",
      "vote_average": 5.7,
      "overview": "타깃 제거 100%, 실패 확률 0%  킬러 ‘에이바’(제시카 차스테인).  프랑스 최대의 사기범을 제거하는 작전에 투입된 그녀는 임무 중 조직의 금기를 깨트린다. 한편, 그 사실을 알게 된 새로운 보스 ‘사이먼’(콜린 파렐)은 그녀를 제거할 것을 명령하게 되는데… 죽거나, 죽이거나 타깃이 된 그녀, 살기 위한 킬링 액션이 시작된다!",
      "release_date": "2020-07-02"
    },
    {
      "popularity": 523.908,
      "vote_count": 778,
      "video": "False",
      "poster_path": "/4m6w5gXggWfxeCZD81Pxb9B4hx5.jpg",
      "id": 581392,
      "adult": "False",
      "backdrop_path": "/gEjNlhZhyHeto6Fy5wWy5Uk3A9D.jpg",
      "original_language": "ko",
      "original_title": "반도",
      "genre_ids": [
        28,
        27,
        53
      ],
      "title": "반도",
      "vote_average": 7,
      "overview": "전대미문의 재난 이후 4년이 흐른 대한민국은 버려진 땅이 되어버렸다. 사람들은 고립된 섬이 된 반도에 갇혔고 누구의 생사도 확인할 수 없는 상황에서 정석은 피할 수 없는 미션을 받고 한국 땅에 다시 발을 들인다. 정석은 미지의 세계인 그곳에서 예상치 못한 습격을 받고 일촉즉발의 순간 ‘반도’의 생존자들을 만나게 된다.",
      "release_date": "2020-07-15"
    },
    {
      "popularity": 532.446,
      "vote_count": 189,
      "video": "False",
      "poster_path": "/m9ZDoCzSbQ7SAOz2tcb1rt6bGG2.jpg",
      "id": 694919,
      "adult": "False",
      "backdrop_path": "/pq0JSpwyT2URytdFG0euztQPAyR.jpg",
      "original_language": "en",
      "original_title": "Money Plane",
      "genre_ids": [
        28
      ],
      "title": "플레인 하이스트",
      "vote_average": 5.9,
      "overview": "마지막 게임에서의 거액의 빚을 갚기 위해 ‘다리우스’ 밑에서 일하게 된 전직 도박꾼 ‘잭’은 전세계 극악무도한 범죄자들이 모여 베팅을 벌이는 ‘머니 플레인’에 탑승해 현금 수백만 달러를 탈취하고 가상 화폐 10억 달러를 해킹하는 미션을 성공시켜야 한다. 하지만 다리우스는 잭을 함정에 빠뜨리고 잭은 플랜B를 가동해 되갚아주려 하는데…!",
      "release_date": "2020-09-29"
    },
    {
      "popularity": 495.392,
      "vote_count": 918,
      "video": "False",
      "poster_path": "/6agKYU5IQFpuDyUYPu39w7UCRrJ.jpg",
      "id": 740985,
      "adult": "False",
      "backdrop_path": "/hbrXbVoE0NuA1ORoSGGYNASagrl.jpg",
      "original_language": "en",
      "original_title": "Borat Subsequent Moviefilm",
      "genre_ids": [
        35
      ],
      "title": "보랏 속편",
      "vote_average": 6.6,
      "overview": "한때 영광스러운 국가였던 카자흐스탄의 이익을 위해 미국 정권에 엄청난 뇌물 전달하기",
      "release_date": "2020-10-23"
    },
    {
      "popularity": 497.673,
      "vote_count": 361,
      "video": "False",
      "poster_path": "/Amkk8KY5Vy81RDrVlDDhd2Ay9ho.jpg",
      "id": 718444,
      "adult": "False",
      "backdrop_path": "/x4UkhIQuHIJyeeOTdcbZ3t3gBSa.jpg",
      "original_language": "en",
      "original_title": "Rogue",
      "genre_ids": [
        28,
        12,
        18,
        53
      ],
      "title": "로그",
      "vote_average": 5.8,
      "overview": "대장 샘이 이끄는 용병팀 로그는 무장 단체 알샤바브에게 납치된 주지사의 딸을 구출하기 위해 남아프리카 공화국으로 파견된다. 가까스로 타깃 구출에 성공하지만 잔혹하고 무자비한 알샤바브의 추격은 계속되고, 치열한 전투 속 생사의 갈림길에 서게 된 로그 팀 앞에 치명적인 미지의 존재가 등장한다.",
      "release_date": "2020-08-20"
    },
    {
      "popularity": 663.205,
      "id": 524047,
      "video": "False",
      "vote_count": 500,
      "vote_average": 7.2,
      "title": "그린랜드",
      "release_date": "2020-07-29",
      "original_language": "en",
      "original_title": "Greenland",
      "genre_ids": [
        28,
        53
      ],
      "backdrop_path": "/2Fk3AB8E9dYIBc2ywJkxk8BTyhc.jpg",
      "adult": "False",
      "overview": "혜성의 지구 충돌 속보를 지켜보던 존과 가족들. 미 항공우주국(NASA)의 예측과 달리 해상으로 떨어졌어야 할 파편은 캘리포니아를 비롯해 세계 대도시로 추락해 세계는 순식간에 혼돈에 빠진다. 지구의 3/4을 날려버릴 초대형 혜성 추락까지 남은 시간은 단 48시간. 존과 가족은 지구의 유일한 안전 대피소인 ‘그린란드’의 벙커로 향하는데... 인류의 마지막 카운트다운이 시작된다!",
      "poster_path": "/sHDXaVkqr46bolDZV757bNxB7sZ.jpg"
    },
    {
      "popularity": 452.038,
      "vote_count": 154,
      "video": "False",
      "poster_path": "/xqvX5A24dbIWaeYsMTxxKX5qOfz.jpg",
      "id": 660982,
      "adult": "False",
      "backdrop_path": "/75ooojtgiKYm5LcCczbCexioZze.jpg",
      "original_language": "en",
      "original_title": "American Pie Presents: Girls' Rules",
      "genre_ids": [
        35
      ],
      "title": "아메리칸 파이: 여자의 규칙",
      "vote_average": 6.2,
      "overview": "",
      "release_date": "2020-10-06"
    },
    {
      "popularity": 409.364,
      "vote_count": 523,
      "video": "False",
      "poster_path": "/kPzcvxBwt7kEISB9O4jJEuBn72t.jpg",
      "id": 677638,
      "adult": "False",
      "backdrop_path": "/pO1SnM5a1fEsYrFaVZW78Wb0zRJ.jpg",
      "original_language": "en",
      "original_title": "We Bare Bears: The Movie",
      "genre_ids": [
        10751,
        16,
        12,
        35
      ],
      "title": "위 베어 베어스: 더 무비",
      "vote_average": 7.7,
      "overview": "그리즐리, 팬더, 아이스 베어가 푸드 트럭을 얼마나 사랑하는지에 대한 바이럴 비디오가 퍼지게 되면서 생긴 사고로 대규모의 정전 사태가 발발한다. 이 사건은 국립 야생 동물 관리국 소속 트라우트 요원의 관심을 끌게 된다. 트라우트는 인간과 같은 생활 방식을 갖고 있는 곰들을 영원히 격리시킴으로써 자연의 질서를 회복하겠다고 선언한다. 정든 집에서 쫓겨 난 곰들은 캐나다에서 피난처를 찾는 과정에서 새로운 친구, 위험한 장애물, 거대한 파티로 가득 찬 여행을 떠난다. 이 위험천만한 여정은 그들이 처음 만나고 형제가 되었던 예전을 돌아보게 하는데...",
      "release_date": "2020-06-30"
    },
    {
      "popularity": 384.702,
      "vote_count": 112,
      "video": "False",
      "poster_path": "/k8Rp9g6kEmlNbNf6Y4fycDCz3uh.jpg",
      "id": 601844,
      "adult": "False",
      "backdrop_path": "/qTrpw2ZUvN7ywUu1kieEsvNDrgQ.jpg",
      "original_language": "en",
      "original_title": "Becky",
      "genre_ids": [
        53,
        28,
        27
      ],
      "title": "벡키",
      "vote_average": 6.4,
      "overview": "아빠와 다툰 후 자신만의 공간에서 홀로 시간을 보내던 십 대 소녀 '벡키'.  같은 시간, 감옥을 탈출한 범죄자들이 무언가를 찾기 위해 벡키의 집으로 들이닥친다. 평소 벡키가 지니고 다니던 열쇠를 찾아, 벡키의 가족들을 위협하는 범죄자들. 그리고 이 사실을 전혀 모르고 있던 백키는 의문의 총소리를 시작으로 혼란에 휩싸이게 되는데...! \"난 너희들을 다치게 할 거야! 기대해도 좋아!\"",
      "release_date": "2020-07-23"
    },
    {
      "popularity": 412.984,
      "id": 734309,
      "video": "False",
      "vote_count": 156,
      "vote_average": 5.6,
      "title": "산타나",
      "release_date": "2020-08-28",
      "original_language": "en",
      "original_title": "Santana",
      "genre_ids": [
        28
      ],
      "backdrop_path": "/7fvdg211A2L0mHddvzyArRuRalp.jpg",
      "adult": "False",
      "overview": "오래전 부모를 살해한 원수. 마약 조직 보스의 숨겨진 정체가 드디어 드러난다. 성격은 다르지만 목적은 같은 형제. 범죄수사국 요원과 장군이 목숨 건 복수를 시작한다.",
      "poster_path": "/9Rj8l6gElLpRL7Kj17iZhrT5Zuw.jpg"
    },
    {
      "popularity": 393.367,
      "vote_count": 230,
      "video": "False",
      "poster_path": "/t28nWRyiwT2cI0KwXYLPwnNltUV.jpg",
      "id": 438396,
      "adult": "False",
      "backdrop_path": "/qGZe9qTuydxyJYQ60XDtEckzLR8.jpg",
      "original_language": "es",
      "original_title": "Orígenes secretos",
      "genre_ids": [
        18,
        53
      ],
      "title": "히어로는 없다",
      "vote_average": 6.2,
      "overview": "히어로는 무슨. 하지만 범죄가 슈퍼히어로 스토리를 빼다 박았다면? 신참 형사가 사건 해결을 위해 공조 아닌 공조를 시작한다. 퍼즐 조각에 불과한 연쇄 살인. 그 큰 그림을 볼 수 있는 건 코믹스라면 꽉 잡은 만화 가게 주인뿐이니까.",
      "release_date": "2020-08-28"
    },
    {
      "popularity": 392.396,
      "id": 475430,
      "video": "False",
      "vote_count": 938,
      "vote_average": 5.8,
      "title": "아르테미스 파울",
      "release_date": "2020-06-12",
      "original_language": "en",
      "original_title": "Artemis Fowl",
      "genre_ids": [
        12,
        14,
        878,
        10751,
        28
      ],
      "backdrop_path": "/o0F8xAt8YuEm5mEZviX5pEFC12y.jpg",
      "adult": "False",
      "overview": "12살 천재 소년 아르테미스 파울은 유서 깊은 범죄 주모자 집안의 후예이다. 사라진 아버지를 찾으려 하던 중 숨어 있던 강력한 요정 종족이 그 실종 사건의 배후일 수 있다는 것을 알게 된다.",
      "poster_path": "/mhDdx7o7hhrxrikq8aqPLLnS9w8.jpg"
    },
    {
      "popularity": 344.863,
      "vote_count": 23,
      "video": "False",
      "poster_path": "/vSfchsOaP6xFrLsG6hzXgc3woZ2.jpg",
      "id": 634244,
      "adult": "False",
      "backdrop_path": "/cw8A0SprTxr7uSfcH7lwSRRhezJ.jpg",
      "original_language": "en",
      "original_title": "Heavenquest: A Pilgrim's Progress",
      "genre_ids": [
        12,
        14,
        28
      ],
      "title": "헤븐퀘스트",
      "vote_average": 6.6,
      "overview": "아주 먼 옛날 위대한 에오스 제국은 어둠의 세력의 부활로 무너지게 되고 북왕국과 남왕국의 천 년 전쟁으로 대혼란에 처한다. 왕의 재판관 '반젤'과 그의 친구들, 여전사 '에즈라', 마법사 '엘더'로 구성된 다섯 명의 선택받은 자들은 평화를 지키기 위해 고대 기록의 예언에 따라 빛과 어둠이 존재하는 타락한 관문을 향해 목숨을 건 여정을 떠난다. 한편, 점점 세력을 키워온 어둠의 세력 '아몬'과의 피할 수 없는 전쟁을 앞둔 다섯 명의 선택받은 자들은 드디어 최후의 전쟁을 시작하는데...",
      "release_date": "2020-07-13"
    },
    {
      "popularity": 303.836,
      "id": 697064,
      "video": "False",
      "vote_count": 24,
      "vote_average": 5.7,
      "title": "어쌔신 프리스트 벡맨",
      "release_date": "2020-09-10",
      "original_language": "en",
      "original_title": "Beckman",
      "genre_ids": [
        28
      ],
      "backdrop_path": "/7WKIOXJa2JjHygE8Yta3uaCv6GC.jpg",
      "adult": "False",
      "overview": "존경 받는 신부 벡맨은 암살자였던 과거를 숨기고 사이비 교단에서 탈출한 타비타를 입양하여 건실하게 살고 있다. 어느날 사이비 교단의 습격으로 타비타는 납치되고 벡맨은 부상을 당한다. 분노한 벡맨은 다시 암살조직에 복귀해 총을 잡게 되고 교단이 고용한 킬러들과 목숨을 건 대결을 벌인다.",
      "poster_path": "/vxJFueYtoDMK40ZwmyUPCiNaeVl.jpg"
    },
    {
      "popularity": 364.107,
      "vote_count": 140,
      "video": "False",
      "poster_path": "/n6hptKS7Y0ZjkYwbqKOK3jz9XAC.jpg",
      "id": 594328,
      "adult": "False",
      "backdrop_path": "/lkeBhXGJFRlhI7cBWn8LQQAdZqK.jpg",
      "original_language": "en",
      "original_title": "Phineas and Ferb The Movie: Candace Against the Universe",
      "genre_ids": [
        16,
        878,
        35,
        10402,
        10751,
        12
      ],
      "title": "피니와 퍼브: 캔디스 대 우주",
      "vote_average": 7.3,
      "overview": "",
      "release_date": "2020-08-28"
    },
    {
      "popularity": 369.253,
      "vote_count": 1587,
      "video": "False",
      "poster_path": "/xDZ0tHXxesM34GGLJxr3CCnwPHU.jpg",
      "id": 605116,
      "adult": "False",
      "backdrop_path": "/qVygtf2vU15L2yKS4Ke44U4oMdD.jpg",
      "original_language": "en",
      "original_title": "Project Power",
      "genre_ids": [
        28,
        80,
        878
      ],
      "title": "프로젝트 파워",
      "vote_average": 6.6,
      "overview": "뉴올리언스에 퍼지기 시작한 의문의 약. 강해지고 싶다면 삼켜라. 5분간 엄청난 초능력이 주어진다. 주의사항은? 약을 먹기 전까진 어떤 초능력이 생길지 모른다는 것. 누군가는 총알도 뚫지 못하는 방탄 피부가 되고, 누군가는 투명 인간이 된다. 그리고 또 누군가는 치명적인 능력을 부여받는다. 하지만 가장 큰 문제는 이 약 때문에 범죄 도시로 변하고 있는 뉴올리언스. 이대로 두고 볼 수 없는 경찰 프랭크는 약의 출처를 뒤쫓는다. 마약상인 10대 소녀와 복수를 위해 비밀리에 움직이는 전직 군인과 함께. 이제 어떤 위험을 감수하더라도 그들을 막아야 한다. 파워를 삼켜서라도.",
      "release_date": "2020-08-14"
    },
    {
      "popularity": 355.314,
      "vote_count": 6314,
      "video": "False",
      "poster_path": "/sshtRdR9B31LAQbYjwljXGaJ9Kz.jpg",
      "id": 495764,
      "adult": "False",
      "backdrop_path": "/9xNOiv6DZZjH7ABoUUDP0ZynouU.jpg",
      "original_language": "en",
      "original_title": "Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn)",
      "genre_ids": [
        28,
        80,
        35
      ],
      "title": "버즈 오브 프레이: 할리 퀸의 황홀한 해방",
      "vote_average": 7.2,
      "overview": "오랜 연인이던 조커와 헤어진 할리 퀸은 처음 맞이한 해방에 황홀함을 느낀다. 하지만 조커라는 방패막이 사라지자 평생 처음 무방비 상태에 놓인 할리 퀸을 고담시에서 가장 비열한 범죄왕 로만 시오니스와 고담의 모든 갱들이 노린다. 통제 불능의 상태에서 카산드라라는 소매치기가 로만의 부하에게서 모든 권력과 고담시 지하 세계 전체의 지배권을 차지할 열쇠인 금융 정보가 암호화되어 있는 다이아몬드를 훔치면서 사건을 걷잡을 수 없이 급변한다. 로만 손에 죽을 위기에 처한 할리 퀸은 헌트리스, 블랙 카나리, 르네 몬토야와 새로운 팀을 결성해 로만에 맞서는데...",
      "release_date": "2020-02-05"
    },
    {
      "popularity": 328.712,
      "vote_count": 46,
      "video": "False",
      "poster_path": "/fD6WrWTL2jzKyFE45jGOIuq5E7g.jpg",
      "id": 635237,
      "adult": "False",
      "backdrop_path": "/sFLgXQGrSWxnjmPOpGKPApWNOUH.jpg",
      "original_language": "en",
      "original_title": "Arthur & Merlin: Knights of Camelot",
      "genre_ids": [
        28,
        12
      ],
      "title": "킹 아더 카멜롯의 기사",
      "vote_average": 6.1,
      "overview": "전쟁에서 승리한 아더 왕은 결투자가 되어 은둔한다. 야욕을 가진 왕자는 귀네비어 왕비와 결혼하여 왕좌를 차지하는 음모를 꾸민다. 아더 왕은 빼앗긴 왕국을 되찾기 위해 원탁의 기사들을 소환해 기사도를 맹세하고 대관식 날에 카멜롯 성을 쳐들어가는데… 전설의 기사들이 귀환한다!",
      "release_date": "2020-05-28"
    },
    {
      "popularity": 335.455,
      "vote_count": 15590,
      "video": "False",
      "poster_path": "/wrCwH6WOvXQvVuqcKNUrLDCDxdw.jpg",
      "id": 475557,
      "adult": "False",
      "backdrop_path": "/n6bUvigpRFqSwmPp1m2YADdbRBc.jpg",
      "original_language": "en",
      "original_title": "Joker",
      "genre_ids": [
        80,
        53,
        18
      ],
      "title": "조커",
      "vote_average": 8.2,
      "overview": "홀어머니와 사는 아서 플렉은 코미디언을 꿈꾸지만 그의 삶은 좌절과 절망으로 가득 차 있다. 광대 아르바이트는 그에게 모욕을 가져다주기 일쑤고, 긴장하면 웃음을 통제할 수 없는 신경병 증세는 그를 더욱 고립시킨다. 정부 예산 긴축으로 인해 정신과 약물을 지원하던 공공의료 서비스마저 없어져 버린 어느 날, 아서는 지하철에서 시비를 걸어온 증권사 직원들에게 얻어맞던 와중에 동료가 건네준 권총으로 그들을 쏴 버리고 만다. 군중들은 지배계급에 대한 저항의 아이콘이 된 그를 추종하기 시작하며 광대 마스크로 얼굴을 가리고 거리로 쏟아져 나오기 시작하는데...",
      "release_date": "2019-10-02"
    },
    {
      "popularity": 333.307,
      "vote_count": 1295,
      "video": "False",
      "poster_path": "/q9KF4CXgK6imiN0Obvg8D7IDRVz.jpg",
      "id": 446893,
      "adult": "False",
      "backdrop_path": "/qsxhnirlp7y4Ae9bd11oYJSX59j.jpg",
      "original_language": "en",
      "original_title": "Trolls World Tour",
      "genre_ids": [
        16,
        10751,
        35,
        14,
        12,
        10402
      ],
      "title": "트롤: 월드 투어",
      "vote_average": 7.5,
      "overview": "노래와 춤을 즐기며 평화로운 나날을 보내던 팝 트롤 파피(안나 켄드릭)와 브랜치(저스틴 팀버레이크) 그리고 친구들. 어느 날 파피는 자신들 외에도 서로 다른 외모와 노래를 가진 5개의 트롤 마을이 더 있다는 것을 알게 된다. 모두와 친구가 되어 신나게 지내고 싶은 파피와 달리 록 트롤 마을의 여왕 바브(레이첼 블룸)는 다른 트롤 마을들을 위협해오고 있다. 바브는 트롤 조상들이 만든 팝, 테크노, 클래식, 컨트리, 펑크, 록 여섯개의 현을 찾아 모든 음악을 통합해, 록을 제외한 음악들을 파괴하려는 위험한 계획을 세운 것. 이를 모르는 팝 트롤들은 다른 음악을 사랑하는 트롤들과도 친구가 될 수 있으리라 믿으며 그들과 어울리기 위한 여행을 떠나는데...",
      "release_date": "2020-03-12"
    },
    {
      "popularity": 317.85,
      "vote_count": 52,
      "video": "False",
      "poster_path": "/tBi5xW9Rd0YoGB0aAggV0EN5LDP.jpg",
      "id": 594718,
      "adult": "False",
      "backdrop_path": "/j9uiJPliO5q6xeBO1Buaeqs2qr0.jpg",
      "original_language": "ru",
      "original_title": "Спутник",
      "genre_ids": [
        878,
        18,
        27
      ],
      "title": "스푸트니크",
      "vote_average": 6.4,
      "overview": "1983년 우주궤도를 돌던 소련의 오르비타-4호가 원인불명의 사고로 불시착하고, 생존한 우주비행사 베시냐코프의 이상징후를 진단하기 위해 뇌전문의인 클리모바가 만국과학연구소로 향한다. 그녀는 악화와 회복을 반복하는 베시냐코프를 진찰하면서, 외계의 기생생물이 그의 몸 안으로 침투하여 불시착과 함께 지구로 왔다는 기밀을 알게 된다. 베시냐코프와 기생생물 사이의 공생관계를 파악한 클리모바는 그를 구하기 위해 또 다른 계획을 꾸민다.",
      "release_date": "2020-09-10"
    },
    {
      "popularity": 343.151,
      "vote_count": 181,
      "video": "False",
      "poster_path": "/eDnHgozW8vfOaLHzfpHluf1GZCW.jpg",
      "id": 606234,
      "adult": "False",
      "backdrop_path": "/u9YEh2xVAPVTKoaMNlB5tH6pXkm.jpg",
      "original_language": "en",
      "original_title": "Archive",
      "genre_ids": [
        878,
        18,
        14,
        53
      ],
      "title": "아카이브",
      "vote_average": 5.9,
      "overview": "2038년 미래 인공 지능을 인간보다 한 단계 더 발전 시키려는 과학자가 불의의 사고를 당한 아내를 죽음으로 부터 불러오는데...",
      "release_date": "2020-08-13"
    },
    {
      "popularity": 338.569,
      "vote_count": 33,
      "video": "False",
      "poster_path": "/4rjHhj1BAREc9zNFU8FheLJQdFf.jpg",
      "id": 621151,
      "adult": "False",
      "backdrop_path": "/5gllGAa3c9UqeRI8r6GXiQJIEtp.jpg",
      "original_language": "en",
      "original_title": "Spell",
      "genre_ids": [
        53,
        27
      ],
      "title": "스펠",
      "vote_average": 5.8,
      "overview": "",
      "release_date": "2020-10-30"
    },
    {
      "popularity": 325.161,
      "id": 722603,
      "video": "False",
      "vote_count": 78,
      "vote_average": 5.8,
      "title": "배틀필드 2025",
      "release_date": "2020-07-07",
      "original_language": "en",
      "original_title": "Battlefield 2025",
      "genre_ids": [
        878,
        27,
        28
      ],
      "backdrop_path": "/m7QpUAeI2xTCJyAVl9J9z5dBTSb.jpg",
      "adult": "False",
      "overview": "",
      "poster_path": "/w6e0XZreiyW4mGlLRHEG8ipff7b.jpg"
    },
    {
      "popularity": 322.771,
      "id": 531499,
      "video": "False",
      "vote_count": 183,
      "vote_average": 6,
      "title": "택스 콜렉터",
      "release_date": "2020-08-07",
      "original_language": "en",
      "original_title": "The Tax Collector",
      "genre_ids": [
        28,
        80,
        18
      ],
      "backdrop_path": "/zogWnCSztU8xvabaepQnAwsOtOt.jpg",
      "adult": "False",
      "overview": "LA 지역 갱들을 관리하며 상납금을 수금하는 최고의 파트너 ‘크리퍼’와 ‘데이비드’. 세상 무서울 것 없는 이들 앞에 조직을 통째로 삼키려는 무법자 ‘코네호’가 나타난다. 지독하고 거칠게 살아남은 두 사람은 조직과 모든 것을 지키기 위해 무자비한 피의 전쟁을 시작하는데…",
      "poster_path": "/yhhJPePGHGtJ6LBVKCyfJg5EBnA.jpg"
    },
    {
      "popularity": 313.679,
      "vote_count": 109,
      "video": "False",
      "poster_path": "/bkld8Me0WiLWipLORRNfF1yIPHu.jpg",
      "id": 624963,
      "adult": "False",
      "backdrop_path": "/ezLKohe4HKsHQbwQwhv0ARo83NC.jpg",
      "original_language": "en",
      "original_title": "A Babysitter's Guide to Monster Hunting",
      "genre_ids": [
        12,
        10751,
        14,
        35
      ],
      "title": "베이비시터를 위한 몬스터 사냥 가이드",
      "vote_average": 6.2,
      "overview": "핼러윈에 날벼락을 맞은 10대 소녀. 돌보던 아이가 납치당했다, 그것도 부기맨과 그의 부하 괴물들에게. 그렇다면 싸우는 수밖에. 베이비시터들의 비밀 결사단이 나가신다!",
      "release_date": "2020-10-14"
    },
    {
      "popularity": 309.592,
      "vote_count": 6101,
      "video": "False",
      "poster_path": "/pMXOlasWr1IzHGH8HWw1ZTXs6rQ.jpg",
      "id": 454626,
      "adult": "False",
      "backdrop_path": "/stmYfCUGd8Iy6kAMBr6AmWqx8Bq.jpg",
      "original_language": "en",
      "original_title": "Sonic the Hedgehog",
      "genre_ids": [
        28,
        878,
        35,
        10751
      ],
      "title": "수퍼 소닉",
      "vote_average": 7.5,
      "overview": "소리보다 빠른 초고속 고슴도치 히어로 '소닉'은 지구에 불시착한다. 그의 특별한 능력을 감지한 과학자 ‘닥터 로보트닉’은 세계 정복의 야욕을 채우려 하고, 경찰관 ‘톰’은 위험에 빠진 ‘소닉’을 돕기 위해 나서는데…! 과연, ‘소닉'은 천재 악당에 맞서 지구를 지킬 수 있을까?",
      "release_date": "2020-02-12"
    },
    {
      "popularity": 329.958,
      "vote_count": 424,
      "video": "False",
      "poster_path": "/nksAuJpMqA3ZtPe3MrlCi8BIg5e.jpg",
      "id": 514207,
      "adult": "False",
      "backdrop_path": "/sizHX5VbwlBihaathTQHVGk1jdi.jpg",
      "original_language": "ru",
      "original_title": "Вторжение",
      "genre_ids": [
        878
      ],
      "title": "인베이젼 2020",
      "vote_average": 7,
      "overview": "첫 우주 침공으로부터 3년이 지난 지구. 인류는 상처를 이겨내고 조금씩 평범한 일상으로 돌아가고 있다. 그러나 평화도 잠시, 다시 그들이 모습을 드러냈다. 물이 존재하는 그 어느 곳도 안전하지 않은 상황. 하지만 인류는 반드시 이겨낼 것이다!",
      "release_date": "2020-01-01"
    },
    {
      "popularity": 322.479,
      "id": 721656,
      "video": "False",
      "vote_count": 76,
      "vote_average": 7.9,
      "title": "해피 할로윈, 스쿠비 두!",
      "release_date": "2020-10-06",
      "original_language": "en",
      "original_title": "Happy Halloween Scooby-Doo!",
      "genre_ids": [
        16,
        10751,
        9648,
        35,
        80
      ],
      "backdrop_path": "/5gTQmnGYKxDfmUWJ9GUWqrszRxN.jpg",
      "adult": "False",
      "overview": "",
      "poster_path": "/5aL71e0XBgHZ6zdWcWeuEhwD2Gw.jpg"
    },
    {
      "popularity": 313.429,
      "id": 592350,
      "video": "False",
      "vote_count": 477,
      "vote_average": 8.5,
      "title": "나의 히어로 아카데미아 더 무비: 히어로즈 라이징",
      "release_date": "2019-12-20",
      "original_language": "ja",
      "original_title": "僕のヒーローアカデミア THE MOVIE ヒーローズ：ライジング",
      "genre_ids": [
        16,
        28
      ],
      "backdrop_path": "/9guoVF7zayiiUq5ulKQpt375VIy.jpg",
      "adult": "False",
      "overview": "눈이 계속 내리는 겨울 어느 밤, 히어로 사회를 파괴하려고 계획하는 시가라키 토무라가 인솔하는 빌런 연합과 그 움직임을 사전에 포착한 히어로들의 전투가 전개되는 가운데, 남모르게 조용히 꿈틀거리는 \"뭔가\"가 일어나고, 그 자리를 떠났다. 마침 이즈쿠 일행의 유에이 고교 히어로과 1학년 A반이 은퇴한 No.1 히어로 올마이트의 뒤를 이어 \"차세대 영웅 육성 프로젝트\"의 일환으로 학급 전원에서 기간 한정의 교외 히어로 활동을 위해 일본의 훨씬 남쪽에 위치한 외딴 섬 \"나부 섬\"을 찾았다. 얼마 전 큰 사건이 일어나지 않았던 평화로운 섬에서 이들은 주재 영웅으로서 섬사람들의 생활을 도우며 분주했고, 그러면서도 한가한 시간을 보내고 있었다. 그러나 그 정적을 부수듯이, 갑자기 빌런들이 나부 섬을 덮쳐, 차례차례로 섬의 시설을 파괴해 간다. 그들을 지휘하는 것은, \"나인\". 그날 밤, 눈을 뜬 \"뭔가\"그 자체였다. 이즈쿠와 바쿠고 등의 1학년 A반의 멤버는 힘을 모아 빌런에 맞선다! 과연 섬을 덮치는 나인의 목적이란!? 그리고 이즈쿠 일행의 1학년 A반의 \"뉴 히어로\"들은 이 가장 흉악한 빌런으로부터 섬의 사람들을 지킬 수 있을까!?",
      "poster_path": "/y56HkHAbSZQJjQaxlqCaRI3lIHu.jpg"
    },
    {
      "popularity": 306.511,
      "vote_count": 379,
      "video": "False",
      "poster_path": "/r4Lm1XKP0VsTgHX4LG4syAwYA2I.jpg",
      "id": 590223,
      "adult": "False",
      "backdrop_path": "/lA5fOBqTOQBQ1s9lEYYPmNXoYLi.jpg",
      "original_language": "en",
      "original_title": "Love and Monsters",
      "genre_ids": [
        28,
        12,
        35,
        878
      ],
      "title": "러브 앤 몬스터즈",
      "vote_average": 7.6,
      "overview": "괴물들로 인해 황폐해진 세상. 몬스터포칼립스가 된 세상에서 죽은 줄로만 알았던 여자친구 에이미의 생존 소식을 라디오로 통해 듣고 그녀를 찾아 다시 세상밖으로 나와 한 마디로 사랑 찾아 모험을 떠나는 청년 조엘의 이야기",
      "release_date": "2020-10-16"
    },
    {
      "popularity": 332.419,
      "vote_count": 5537,
      "video": "False",
      "poster_path": "/anhvhTzdjzMLzGV8oTFNssvMTIw.jpg",
      "id": 38700,
      "adult": "False",
      "backdrop_path": "/upUy2QhMZEmtypPW3PdieKLAHxh.jpg",
      "original_language": "en",
      "original_title": "Bad Boys for Life",
      "genre_ids": [
        53,
        28,
        80
      ],
      "title": "나쁜 녀석들: 포에버",
      "vote_average": 7.3,
      "overview": "마이애미 강력반의 베테랑 형사 ‘마이크’(윌 스미스)는 여전히 범죄자를 소탕하는 데 열성적이지만, 그의 파트너 ‘마커스’(마틴 로렌스)는 이제 일선에서 물러나 가족과 함께 시간을 보내고 싶어한다. 마커스의 은퇴를 만류하던 마이크가 정체를 알 수 없는 거대 조직의 위협을 받으며 일생일대의 위험에 빠지게 된다. 가족만큼 중요한 마이크를 위해 마커스가 합류하고, 우리의 ‘나쁜 녀석들’은 신식 무기와 기술을 장착한 루키팀 AMMO와 함께 힘을 합쳐 일생일대 마지막 미션을 수행하게 되는데…",
      "release_date": "2020-01-15"
    },
    {
      "popularity": 323.654,
      "vote_count": 6449,
      "video": "False",
      "poster_path": "/lVcwSnzhSMWYXUQzyMilCztSE6I.jpg",
      "id": 330457,
      "adult": "False",
      "backdrop_path": "/xJWPZIYOEFIjZpBL7SVBGnzRYXp.jpg",
      "original_language": "en",
      "original_title": "Frozen II",
      "genre_ids": [
        16,
        10751,
        12,
        35,
        14
      ],
      "title": "겨울왕국 2",
      "vote_average": 7.3,
      "overview": "평화를 되찾은 아렌델 왕국에 새로운 위기가 찾아온다. 어느 날부턴가 의문의 목소리가 엘사를 부르고, 평화로운 아렌델 왕국을 위협한다. 트롤은 모든 것은 과거에서 시작되었음을 알려주며 엘사의 힘의 비밀과 진실을 찾아 떠나야한다고 조언한다. 위험에 빠진 아렌델 왕국을 구해야만 하는 엘사와 안나는 숨겨진 과거의 진실을 찾아 크리스토프, 올라프, 그리고 스벤과 함께 위험천만한 놀라운 모험을 떠나게 된다. 자신의 힘을 두려워했던 엘사는 이제 이 모험을 헤쳐나가기에 자신의 힘이 충분하다고 믿어야만 하는데...",
      "release_date": "2019-11-20"
    },
    {
      "popularity": 250.93,
      "id": 721452,
      "video": "False",
      "vote_count": 119,
      "vote_average": 7.1,
      "title": "원 나이트 인 방콕",
      "release_date": "2020-08-25",
      "original_language": "en",
      "original_title": "One Night in Bangkok",
      "genre_ids": [
        28,
        53
      ],
      "backdrop_path": "/riDrpqQtZpXGeiJdlmfcwwPH7nN.jpg",
      "adult": "False",
      "overview": "음주 운전자가 낸 교통사고로 죽임을 당하고 억울하게 누명까지 쓴 딸과 가족, 카이는 복수와 정의 실현을 위해 사고를 내고 사건의 조작에 연루된 변호사, 경찰, 도미닉과 그의 부모, 뒷수습을 한 일본인 등 7명을 찾아간다.",
      "poster_path": "/i4kPwXPlM1iy8Jf3S1uuLuwqQAV.jpg"
    },
    {
      "popularity": 200.572,
      "id": 531876,
      "video": "False",
      "vote_count": 436,
      "vote_average": 6.7,
      "title": "아웃포스트",
      "release_date": "2020-06-24",
      "original_language": "en",
      "original_title": "The Outpost",
      "genre_ids": [
        10752,
        18,
        36,
        28
      ],
      "backdrop_path": "/n1RohH2VoK1CdVI2fXvcP19dSlm.jpg",
      "adult": "False",
      "overview": "사방이 산으로 둘러싸인 방어 불가 지상 최악의 전초기지! 적의 공격에 무방비하게 노출될 수밖에 없는 이곳 아군의 지원은 물론 제대로 된 보급조차 기대하기 힘들다. 군 조사단조차 ‘명백히 방어 불가능’ 이라는 판정을 내린 상태. 호시탐탐 기회를 엿보는 적들로, 매일매일이 위험한 상황 속 총공세가 시작되는데…",
      "poster_path": "/xO6M5dykvcgVhnnBgyW4CxEcy0C.jpg"
    },
    {
      "popularity": 271.962,
      "id": 524216,
      "video": "False",
      "vote_count": 42,
      "vote_average": 6.6,
      "title": "영안실의 미스테리",
      "release_date": "2020-10-08",
      "original_language": "en",
      "original_title": "The Mortuary Collection",
      "genre_ids": [
        14,
        27
      ],
      "backdrop_path": "/tsGSTBl5H8DBLnHc24Teny0Ppc5.jpg",
      "adult": "False",
      "overview": "샘은 어느 별난 노인이 운영하는 외딴 영안실을 찾아가 자신을 조수로 일하게 해달라고 부탁하는 특이한 젊은 여성이다. 노인과 간단한 인터뷰를 마친 샘은 노인에게 장의사로 영안실에서 일하면서 그가 겪은 가장 무서운 이야기를 해달라고 한다. 노인은 샘에게 1950년대부터 19880년대까지 불길한 비밀을 다룬 네 가지 이야기를 들려준다.",
      "poster_path": "/5WXeYnezavNI6hXH74aQYv6yFzj.jpg"
    },
    {
      "popularity": 262.132,
      "vote_count": 219,
      "video": "False",
      "poster_path": "/xOmGTJtBgRVSAF4S5dZEUqHqyy5.jpg",
      "id": 621870,
      "adult": "False",
      "backdrop_path": "/oSSEcPDfwgZSv2i01Oqxdb9t8fI.jpg",
      "original_language": "en",
      "original_title": "Secret Society of Second Born Royals",
      "genre_ids": [
        28,
        12,
        35,
        14
      ],
      "title": "시크릿 소사이어티 오브 세컨드 본 로얄",
      "vote_average": 7,
      "overview": "왜? 동화책에는 장남과 장녀, 또는 외동아들과 외동딸 얘기만 있을까? 형, 언니가 왕이 되고 왕비가 되고 콩고물조차 얻어먹지 못해 서러운 둘째 아이들은 동화책에서까지 존재조차 완전히 지워지곤 한다. 왜냐면, 둘째 아이들은 특별한 능력을 지니고 태어나기 때문. 슈퍼히어로 못지 않은 능력으로 동화책 속 왕국을 보호하는 임무를 수행하기 때문에 그들의 존재를 그 누구도 알아서는 안되기 때문이다. 더이상 서럽지 않은 둘째 아이들의 특별한 이야기가 시작된다.",
      "release_date": "2020-09-25"
    },
    {
      "popularity": 251.857,
      "id": 630566,
      "video": "False",
      "vote_count": 344,
      "vote_average": 8.4,
      "title": "클라우즈",
      "release_date": "2020-10-09",
      "original_language": "en",
      "original_title": "Clouds",
      "genre_ids": [
        10402,
        18,
        10749
      ],
      "backdrop_path": "/bx326cwBtDsfDcnTgFlK5dXkyaC.jpg",
      "adult": "False",
      "overview": "",
      "poster_path": "/2YvT3pdGngzpbAuxamTz4ZlabnT.jpg"
    },
    {
      "popularity": 254.157,
      "vote_count": 104,
      "video": "False",
      "poster_path": "/4BgSWFMW2MJ0dT5metLzsRWO7IJ.jpg",
      "id": 726739,
      "adult": "False",
      "backdrop_path": "/t22fWbzdnThPseipsdpwgdPOPCR.jpg",
      "original_language": "en",
      "original_title": "Cats & Dogs 3: Paws Unite",
      "genre_ids": [
        35,
        28
      ],
      "title": "캣츠 앤 독스 3: 퍼스 유나이트",
      "vote_average": 6.6,
      "overview": "",
      "release_date": "2020-10-02"
    },
    {
      "popularity": 392.72,
      "vote_count": 13,
      "video": "False",
      "poster_path": "/frB57nMDmu4NnSzjmrq0lEx5iod.jpg",
      "id": 658412,
      "adult": "False",
      "backdrop_path": "/41OpRg2VZAwzETbwrWtzyF5vACi.jpg",
      "original_language": "hi",
      "original_title": "लूडो",
      "genre_ids": [
        80,
        35
      ],
      "title": "루도 - 인생 게임",
      "vote_average": 7.2,
      "overview": "지우고 싶은 동영상부터 위험천만한 돈 가방까지. 인생을 바꾸려는 네 명의 플레이어가 운명의 게임에 얽혀든다. 판을 좌우하는 건 인생이란 주사위. 당신은 삶을 바꿀 용기가 있는가.",
      "release_date": "2020-11-12"
    },
    {
      "popularity": 260.492,
      "vote_count": 20171,
      "video": "False",
      "poster_path": "/kmP6viwzcEkZeoi1LaVcQemcvZh.jpg",
      "id": 299536,
      "adult": "False",
      "backdrop_path": "/lmZFxXgJE3vgrciwuDib0N8CfQo.jpg",
      "original_language": "en",
      "original_title": "Avengers: Infinity War",
      "genre_ids": [
        12,
        28,
        878
      ],
      "title": "어벤져스: 인피니티 워",
      "vote_average": 8.3,
      "overview": "타노스는 6개의 인피니티 스톤을 획득해 신으로 군림하려 한다. 그것은 곧 인류의 절반을 학살해 우주의 균형을 맞추겠다는 뜻. 타노스는 닥터 스트레인지가 소유한 타임 스톤, 비전의 이마에 박혀 있는 마인드 스톤을 차지하기 위해 지구를 침략한다. 아이언맨과 스파이더맨은 가디언즈 오브 갤럭시의 멤버들과 타노스를 상대한다. 지구에선 캡틴 아메리카, 완다, 블랙 위도우, 블랙 팬서 등이 비전을 지키기 위해 뭉친다.",
      "release_date": "2018-04-25"
    },
    {
      "popularity": 260.058,
      "vote_count": 0,
      "video": "False",
      "poster_path": "/n15reqf2NvUq13mSUOeYftMnBd1.jpg",
      "id": 283566,
      "adult": "False",
      "backdrop_path": "/cdav7lVUviYvQwKB2v73PpaJMFV.jpg",
      "original_language": "ja",
      "original_title": "シン・エヴァンゲリオン劇場版:||",
      "genre_ids": [
        28,
        16,
        18,
        878
      ],
      "title": "신 에반게리온 극장판 :||",
      "vote_average": 0,
      "overview": "",
      "release_date": "2021-01-23"
    },
    {
      "popularity": 260.687,
      "vote_count": 125,
      "video": "False",
      "poster_path": "/gEIcPyNduE28kNTMlQ5QN1rbbt7.jpg",
      "id": 425001,
      "adult": "False",
      "backdrop_path": "/a9jZrU7LJk6mAUjmkbEmTiC52l0.jpg",
      "original_language": "en",
      "original_title": "The War with Grandpa",
      "genre_ids": [
        35,
        10751,
        18
      ],
      "title": "워 위드 그랜파",
      "vote_average": 5.9,
      "overview": "할아버지 ‘에드’에게 방을 뺏겨 다락방 신세가 된 손자 ‘피터’.  방을 되찾기 위해 할아버지를 골탕 먹이려 하지만 호락호락하지 않다. 계속되는 ‘피터’의 도발에 ‘에드’의 반격이 시작되고,  방을 사수하기 위한 소리 없는 전쟁이 시작되는데…!",
      "release_date": "2020-08-27"
    }
]

dump=[]

for genre in result_genres:
  dump.append(
    {
      "model":"movie.Genre",
      "id":genre.get('id'),
      "fields":{
        "id":genre.get('id'),
        "name":genre.get('name'),
      }
    }
  )

# print(result[0].get("title"))
for i in range(len(result)):
  dump.append(
    {
      "model":"movie.Movie",
      "fields": {
        "id":result[i].get("id"),
        "title":result[i].get("title"),
        "release_date":result[i].get("release_date"),
        "popularity":result[i].get("popularity"),
        "vote_count":result[i].get("vote_count"),
        "vote_average":result[i].get("vote_average"),
        "overview":result[i].get("overview"),
        "poster_path":f'https://image.tmdb.org/t/p/w300{result[i].get("poster_path")}',
        "genre_ids":result[i].get("genre_ids"),
      }
    }
  )


with open('movies.json','w', encoding='UTF-8') as file:
  file.write(json.dumps(dump, indent=2, ensure_ascii=False))

