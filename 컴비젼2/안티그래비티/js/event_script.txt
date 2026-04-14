// Mock Data for Events
const events = [
    {
        id: 1,
        title: "2026 서울 비전 불꽃축제",
        category: "festival",
        region: "서울",
        date: "2026.10.03",
        location: "서울 여의도 한강공원",
        description: "전 세계 팀들이 참여하는 화려한 불꽃의 향연이 밤하늘을 수놓습니다.",
        fullDescription: "서울의 밤하늘을 수놓는 세계 최고의 불꽃 축제에 초대합니다.\n\n매년 수백만 명의 시민들이 찾는 '서울 비전 불꽃축제'는 단순한 불꽃놀이를 넘어 화합과 희망의 메시지를 전달합니다. 올해는 전 세계 5개국 정상급 불꽃 팀이 참여하여 각국의 문화를 화려한 불꽃과 음악으로 표현할 예정입니다.\n\n다양한 사전 행사와 푸드트럭, 공연이 준비되어 있으니 가족, 연인과 함께 잊지 못할 추억을 만들어보세요.",
        image: "https://images.unsplash.com/photo-1467810563316-b5476525c0f9?q=80&w=2069&auto=format&fit=crop",
        tag: "인기축제"
    },
    {
        id: 2,
        title: "K-리그 올스타전 2026",
        category: "sports",
        region: "서울",
        date: "2026.07.15",
        location: "서울 월드컵 경기장",
        description: "국내 최고의 축구 스타들이 한자리에 모여 펼치는 환상적인 경기.",
        fullDescription: "대한민국 축구의 별들이 한자리에 모이는 최고의 축제!\n\nK-리그를 대표하는 최고의 선수들이 모여 축구 팬들에게 잊지 못할 박진감 넘치는 경기를 선사합니다. 단순한 승패를 넘어선 화려한 개인기와 팬 서비스, 그리고 다양한 이벤트가 준비되어 있습니다.\n\n올스타전만의 특별한 유니폼과 굿즈 판매, 선수들과의 팬 미팅 세션도 놓치지 마세요.",
        image: "sports_event_img_1769768758965.png",
        tag: "빅매치"
    },
    {
        id: 3,
        title: "부산 국제 락 페스티벌",
        category: "festival",
        region: "경상",
        date: "2026.08.10 - 08.12",
        location: "부산 삼락생태공원",
        description: "끊이지 않는 음악과 젊음의 열기, 대한민국 대표 락 페스티벌.",
        fullDescription: "아시아 최고의 락 페스티벌, 부산의 열정은 멈추지 않는다!\n\n국내외 정상급 아티스트들이 대거 참여하는 3일간의 무한 질주. 삼락생태공원의 탁 트인 자연 속에서 즐기는 음악과 맥주, 그리고 캠핑까지. 일상의 스트레스를 날려버릴 최고의 여름 휴가지를 제안합니다.\n\n올해는 더욱 강력해진 사운드 시스템과 넓어진 스테이지로 여러분을 찾아갑니다.",
        image: "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?q=80&w=2070&auto=format&fit=crop",
        tag: "여름한정"
    },
    {
        id: 4,
        title: "2026 강릉 단오제",
        category: "culture",
        region: "강원",
        date: "2026.06.20 - 06.27",
        location: "강릉 남대천 일원",
        description: "유네스코 인류무형문화유산으로 지정된 한국 최고의 전통 축제.",
        fullDescription: "천년의 축제, 유네스코 인류무형문화유산 '강릉 단오제'.\n\n조상들의 지혜와 전통이 살아 숨 쉬는 한국의 대표 축제입니다. 대관령 국사성황신을 모셔오는 영신행차를 시작으로, 신명 나는 가면극, 굿, 농악 등 다양한 전통 예술 공연이 펼쳐집니다.\n\n또한 전국 최대 규모의 난장이 서며, 단오 수리취떡 먹기, 창포물 머리 감기 등 고유의 민속 체험을 통해 우리 문화의 정취를 듬뿍 느껴보실 수 있습니다.",
        image: "gangneung_danoje_img_1769770152086.png",
        tag: "전통문화"
    },
    {
        id: 5,
        title: "Lck 서머 파이널",
        category: "sports",
        region: "경기",
        date: "2026.09.05",
        location: "일산 킨텍스",
        description: "전 세계 팬들이 주목하는 리그 오브 레전드 챔피언스 코리아 결승전.",
        fullDescription: "왕좌를 향한 마지막 전투, LCK Summer Final!\n\n수개월 동안 치열하게 달려온 정규 시즌과 플레이오프의 종착역. 대한민국 최고의 두 팀이 우승 컵과 월드 챔피언십 진출권을 두고 최후의 결전을 벌입니다.\n\n현장에서만 느낄 수 있는 압도적인 함성, 팀별 응원전, 그리고 다양한 스폰서 부스 이벤트를 놓치지 마세요. 전 세계 E-스포츠 역사가 새로 쓰이는 이 순간의 주인공이 되어보세요.",
        image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=2070&auto=format&fit=crop",
        tag: "E-스포츠"
    },
    {
        id: 6,
        title: "제주 유채꽃 축제",
        category: "festival",
        region: "제주",
        date: "2026.04.01 - 04.10",
        location: "제주 서귀포시 표선면",
        description: "노란 유채꽃 물결 속에서 봄의 시작을 느껴보세요.",
        fullDescription: "꽃향기 가득한 제주의 봄, 유채꽃의 향연.\n\n서귀포시 표선면 가시리 '녹산로'를 따라 펼쳐지는 끝없는 유채꽃 길은 한국에서 가장 아름다운 도로 중 하나로 손꼽힙니다. 파란 하늘과 대비되는 선명한 노란 유채꽃 물결 속에서 잊지 못할 사진을 남겨보세요.\n\n다양한 버스킹 공연과 지역 먹거리 체험, 유채꽃 꽃차 만들기 등 봄의 정취를 만끽할 수 있는 다채로운 프로그램이 준비되어 있습니다.",
        image: "https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=2070&auto=format&fit=crop",
        tag: "봄나들이"
    },
    {
        id: 7,
        title: "2026 월드 DJ 페스티벌",
        category: "concert",
        region: "서울",
        date: "2026.06.15 - 06.16",
        location: "서울랜드",
        description: "국내외 정상급 DJ들이 선사하는 뜨거운 EDM의 밤.",
        fullDescription: "폭발적인 비트, 환상적인 레이저 쇼! EDM 마니아들의 성지.\n\n매년 전 세계 정상급 DJ 라인업을 자랑하는 월드 DJ 페스티벌이 역대급 규모로 돌아왔습니다. 서울랜드를 화려하게 물들일 압도적인 비주얼 아트와 사운드 퍼포먼스.\n\n낮부터 밤까지 이어지는 논스톱 파티에서 자유로운 에너지를 발산해보세요. 당신의 심장박동을 깨울 2026년 최고의 순간이 찾아옵니다.",
        image: "https://images.unsplash.com/photo-1459749411177-042180ce673c?q=80&w=2070&auto=format&fit=crop",
        tag: "매진임박"
    },
    {
        id: 8,
        title: "인천 펜타포트 락 페스티벌",
        category: "concert",
        region: "인천",
        date: "2026.08.05 - 08.07",
        location: "인천 송도달빛축제공원",
        description: "대한민국 락 정신의 자존심, 펜타포트와 함께하는 3일간의 여정.",
        fullDescription: "Born to be Wild! 대한민국 락의 역사와 미래를 만나다.\n\n송도의 푸른 하늘 아래 펼쳐지는 강렬한 기타 리프와 드럼 비트. 세대를 아우르는 전설적인 락 밴드부터 차세대 인디 밴드까지, 음악에 대한 갈증을 시원하게 해결해줄 라인업이 준비되어 있습니다.\n\n자유로운 피크닉 구역과 캠핑 존에서 진정한 페스티벌 라이프를 경험해보세요. 펜타포트는 단순한 공연을 넘어선 하나의 문화입니다.",
        image: "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?q=80&w=2070&auto=format&fit=crop",
        tag: "티켓오픈"
    },
    {
        id: 9,
        title: "제주 뮤직 월드 페스티벌",
        category: "concert",
        region: "제주",
        date: "2026.11.12",
        location: "제주 컨벤션센터",
        description: "아름다운 제주에서 만나는 글로벌 뮤지션들의 환상적인 공연.",
        fullDescription: "섬 전체가 무대가 되는 매혹적인 음악 여행.\n\n제주의 신비로운 자연과 어우러지는 감성적이고 파격적인 뮤직 퍼포먼스. 팝, 재즈, 크로스오버를 넘나드는 글로벌 뮤지션들이 제주 컨벤션센터에 모여 환상적인 밤을 선사합니다.\n\n아름다운 야경과 함께 즐기는 와인 시음회, 아티스트 토크 등 품격 있는 부대 행사들이 당신을 기다리고 있습니다.",
        image: "https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?q=80&w=1974&auto=format&fit=crop",
        tag: "NEW"
    }
];

// Review Data
let reviews = JSON.parse(localStorage.getItem('eventReviews')) || {};

// Filter State
let currentRegion = '전체';
let currentCategory = 'all';

// DOM Elements
const eventsGrid = document.querySelector('.events-grid');
const searchInput = document.querySelector('.search-box input');
const searchButton = document.querySelector('.search-box button');
const categoryCards = document.querySelectorAll('.category-card');
const regionButtons = document.querySelectorAll('.region-btn');

// Detail Modal Elements
const modal = document.getElementById('reviewModal');
const modalInner = document.querySelector('.modal-content');
const modalImg = document.getElementById('modalEventImg');
const modalTag = document.getElementById('modalEventTag');
const modalTitle = document.getElementById('modalEventTitle');
const modalDate = document.getElementById('modalEventDate');
const modalLocation = document.getElementById('modalEventLocation');
const modalDesc = document.getElementById('modalEventDesc');

const reviewText = document.getElementById('reviewText');
const reviewList = document.getElementById('reviewList');
const submitBtn = document.getElementById('submitReview');
const closeModal = document.querySelector('.close-modal');

let currentEventId = null;

// Function to Create Event Cards
function displayEvents() {
    const query = searchInput.value.toLowerCase();

    const filtered = events.filter(event => {
        const matchesRegion = currentRegion === '전체' || event.region === currentRegion;
        const matchesCategory = currentCategory === 'all' || event.category === currentCategory;
        const matchesSearch = event.title.toLowerCase().includes(query) ||
            event.location.toLowerCase().includes(query) ||
            event.description.toLowerCase().includes(query);

        return matchesRegion && matchesCategory && matchesSearch;
    });

    eventsGrid.innerHTML = '';

    if (filtered.length === 0) {
        eventsGrid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; font-size: 1.2rem; padding: 2rem; color: var(--text-gray);">일치하는 행사가 없습니다.</p>';
        return;
    }

    filtered.forEach(event => {
        const card = document.createElement('div');
        card.className = 'event-card';
        card.innerHTML = `
            <div class="event-image" style="background-image: url('${event.image}')">
                <span class="event-tag">${event.tag}</span>
            </div>
            <div class="event-content">
                <p class="event-date">${event.date}</p>
                <h3>${event.title}</h3>
                <p>${event.description}</p>
                <div class="event-footer">
                    <span class="location"><i class="fas fa-map-marker-alt"></i> ${event.location}</span>
                    <button class="btn-more" onclick="openDetailModal(${event.id})">상세보기 & 후기</button>
                </div>
            </div>
        `;
        eventsGrid.appendChild(card);
    });
}

// Detail View Logic
function openDetailModal(id) {
    const event = events.find(e => e.id === id);
    if (!event) return;

    currentEventId = id;

    // Populate Details
    modalImg.style.backgroundImage = `url('${event.image}')`;
    modalTag.innerText = event.tag;
    modalTitle.innerText = event.title;
    modalDate.innerText = event.date;
    modalLocation.innerText = event.location;
    modalDesc.innerText = event.fullDescription || event.description;

    // Reset Scroll Position
    modalInner.scrollTop = 0;

    modal.style.display = 'flex';
    renderReviews();
}

function renderReviews() {
    reviewList.innerHTML = '';
    const eventReviews = reviews[currentEventId] || [];

    if (eventReviews.length === 0) {
        reviewList.innerHTML = '<p style="text-align: center; color: var(--text-gray); padding: 2rem;">아직 후기가 없습니다. 첫 번째 주인공이 되어보세요!</p>';
        return;
    }

    eventReviews.forEach(rev => {
        const item = document.createElement('div');
        item.className = 'review-item';
        item.innerHTML = `
            <span class="reviewer"><i class="fas fa-user-circle"></i> ${rev.user}</span>
            <p>${rev.text}</p>
        `;
        reviewList.appendChild(item);
    });
}

submitBtn.addEventListener('click', () => {
    const isLoggedIn = localStorage.getItem('isLoggedIn');
    if (!isLoggedIn) {
        alert('로그인이 필요한 서비스입니다. 로그인 페이지로 이동합니다.');
        window.location.href = '이벤트로그인.html';
        return;
    }

    const text = reviewText.value.trim();
    if (!text) {
        alert('후기 내용을 입력해주세요.');
        return;
    }

    const username = localStorage.getItem('username') || '익명';

    if (!reviews[currentEventId]) reviews[currentEventId] = [];
    reviews[currentEventId].push({ user: username, text: text });

    localStorage.setItem('eventReviews', JSON.stringify(reviews));
    reviewText.value = '';
    renderReviews();
});

closeModal.onclick = () => modal.style.display = 'none';
window.onclick = (e) => { if (e.target == modal) modal.style.display = 'none'; };

// Filter Logic Hooks
regionButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        regionButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentRegion = btn.getAttribute('data-region').trim().replace(/.*?\s/, ''); // Handle icons
        // Correcting the trim for the icon text
        const actualRegion = btn.innerText.replace(/[^\uAC00-\uD7A3]/g, '').trim();
        currentRegion = actualRegion;
        displayEvents();
    });
});

categoryCards.forEach(card => {
    card.addEventListener('click', () => {
        currentCategory = card.getAttribute('data-category');
        categoryCards.forEach(c => c.style.borderColor = 'transparent');
        card.style.borderColor = 'var(--secondary-color)';
        displayEvents();
    });
});

searchButton.addEventListener('click', displayEvents);
searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') displayEvents();
});

// Navigation Menu Filter Logic
const navItems = document.querySelectorAll('.nav-item');
navItems.forEach(item => {
    item.addEventListener('click', (e) => {
        const filter = item.getAttribute('data-filter');
        if (!filter) return;

        currentCategory = filter;

        // Update category card UI to match
        categoryCards.forEach(c => {
            const cardCat = c.getAttribute('data-category');
            if (cardCat === filter) {
                categoryCards.forEach(card => card.style.borderColor = 'transparent');
                c.style.borderColor = 'var(--secondary-color)';
            }
        });

        displayEvents();
    });
});

// Initial Display
document.addEventListener('DOMContentLoaded', () => {
    displayEvents();
});
