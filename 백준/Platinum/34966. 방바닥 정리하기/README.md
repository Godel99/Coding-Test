# [Platinum V] 방바닥 정리하기 - 34966 

[문제 링크](https://www.acmicpc.net/problem/34966) 

### 성능 요약

메모리: 190456 KB, 시간: 752 ms

### 분류

구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 최단 경로, 격자 그래프

### 제출 일자

2026년 2월 28일 10:38:33

### 문제 설명

<p>구름이는 크기 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi><mo>×</mo><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N \times N$</span></mjx-container>의 정사각형의 방에 거주하고 있다. 어느 날, 구름이는 자신의 방이 방바닥에 놓여있는 물건들로 인해 매우 더럽다는 사실을 깨달았다. 하지만 방바닥의 물건들을 정리하기에는 너무 귀찮았기 때문에, 대신 방바닥에 놓인 <strong>구멍</strong>들을 활용해 물건을 모두 제거하기로 했다.</p>

<p>구름이의 방에 있는 물건과 방바닥에 있는 구멍은 모두 한 칸을 차지하며, 각각은 고유한 색을 가지고 있다. 구름이는 아래와 같은 <strong>시행</strong>을 반복하여 모든 물건들을 제거할 계획이다.</p>

<ol>
<li>구멍 중 하나를 선택해 원하는 만큼 상하좌우로 움직인다.</li>
<li>이동 과정에서 같은 색의 물건이 이동 경로에 있다면, 그 물건은 구멍에 빠져 <b>제거</b>된다. 단, 이동 중에 다른 색의 물건은 지나갈 수 없다.</li>
<li>다른 구멍은 통과하여 지나갈 수 있지만, 이동이 끝난 시점에 두 개 이상의 구멍이 같은 칸에 겹쳐 있으면 안 된다.</li>
<li>이동을 정지하게 되면 해당 시행이 끝나고, 방바닥에 남아있는 물건이 없는 경우에도 해당 시행이 끝난다.</li>
</ol>

<p>만사가 귀찮은 구름이는 최소한의 시행으로 모든 물건을 제거해 방을 깨끗하게 만들고 싶다. 구름이를 도와 구름이의 방의 상태가 주어질 때, <strong>방의 모든 물건을 제거하는 최소 시행 횟수</strong>를 구해주자.</p>

### 입력 

 <p>첫 번째 줄에 방의 크기를 나타내는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>과 색의 수를 나타내는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>M</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$M$</span></mjx-container>이 공백으로 구분되어 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 1 \, 000$</span></mjx-container>; <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>M</mi><mo>≤</mo><mn>2</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq M \leq 2$</span></mjx-container>)</p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 줄에 걸쳐 구름이의 방 상태가 주어진다. 비어있는 칸은 <span style="color:#e74c3c;"><code>.</code></span>으로, 물건은 소문자 알파벳으로, 구멍은 대문자 알파벳으로 주어진다. 같은 색의 구멍이 없는 물건은 없으며, 구멍끼리 색이 같은 경우도 존재하지 않는다.</p>

<p>알파벳은 색을 나타내며, 문자 하나의 대소문자 쌍이 한 가지 색을 나타낸다. 예를 들어, <span style="color:#e74c3c;"><code>A</code></span>와 <span style="color:#e74c3c;"><code>a</code></span>는 같은 색이고, <span style="color:#e74c3c;"><code>A</code></span>는 구멍을 <span style="color:#e74c3c;"><code>a</code></span>는 물건을 나타낸다. 색상은 <span style="color:#e74c3c;"><code>A</code></span>와 <span style="color:#e74c3c;"><code>a</code></span>, 그리고 <span style="color:#e74c3c;"><code>B</code></span>와 <span style="color:#e74c3c;"><code>b</code></span>만을 사용한다.</p>

### 출력 

 <p>첫 번째 줄에 모든 물건을 제거하기 위한 최소 시행 횟수를 출력하라. 만약, 시행을 반복해도 모든 물건을 제거할 수 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 출력하라.</p>

