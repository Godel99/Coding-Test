# [Gold V] Monster Path (Small) - 14306 

[문제 링크](https://www.acmicpc.net/problem/14306) 

### 성능 요약

메모리: 2032 KB, 시간: 0 ms

### 분류

백트래킹, 브루트포스 알고리즘, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 수학, 확률론

### 제출 일자

2026년 2월 3일 11:41:31

### 문제 설명

<p>Codejamon is a mobile game in which monster trainers walk around in the real world to catch monsters. You have an old smartphone with a short battery life, so you need to choose your path carefully to catch as many monsters as possible.</p>

<p>Suppose the Codejamon world is a rectangular grid with R rows and C columns. Rows are numbered from top to bottom, starting from 0; columns are numbered from left to right, starting from 0. You start in the cell in the R<sub>s</sub>th row and the C<sub>s</sub>th column. You will take a total of S unit steps; each step must be to a cell sharing an edge (not just a corner) with your current cell.</p>

<p>Whenever you take a step into a cell in which you have not already caught a monster, you will catch the monster in that cell with probability P if the cell has a monster attractor, or Q otherwise. If you do catch the monster in a cell, it goes away, and you cannot catch any more monsters in that cell, even on future visits. If you do not catch the monster in a cell, you may still try to catch the monster on a future visit to that cell. The starting cell is special: you have no chance of catching a monster there before taking your first step.</p>

<p>If you plan your path optimally before making any move, what is the maximum possible expected number of monsters that you will be able to catch?</p>

<p>The battery can only support limited steps, so hurry up!</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow.</p>

<p>Each test case starts with a line of five integers: R, C, R<sub>s</sub>, C<sub>s</sub> and S. R and C are the numbers of rows and columns in the grid; R<sub>s</sub> and C<sub>s</sub><br>
are the numbers of the row and column of your starting position, and S is the number of steps you are allowed to take.</p>

<p>The next line contains two decimals P and Q, where P is the probability of meeting a monster in cells with a monster attractor, and Q is the probability of meeting a monster in cells without a monster attractor. P and Q are each given to exactly four decimal places.</p>

<p>Each of the next R lines contains contains C space-separated characters; the j-th character of the i-th line represents the cell at row i and column j. Each element is either <code>.</code> (meaning there is no attractor in that cell) or <code>A</code> (meaning there is an attractor in that cell).</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ T ≤ 100.</li>
	<li>0 ≤ R<sub>s</sub> < R.</li>
	<li>0 ≤ C<sub>s</sub> < C.</li>
	<li>0 ≤ Q < P ≤ 1.</li>
	<li>1 ≤ R ≤ 10.</li>
	<li>1 ≤ C ≤ 10.</li>
	<li>0 ≤ S ≤ 5.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the largest possible expected number of monsters that the player can catch in the given amount of steps.</p>

<p><code>y</code> will be considered correct if <code>y</code> is within an absolute or relative error of 10<sup>-6</sup> of the correct answer. </p>

