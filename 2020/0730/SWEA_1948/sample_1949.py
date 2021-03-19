dy=[1,-1,0,0]
dx=[0,0,-1,1]
chk=[0]

for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
def solve(y,x,cur):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(ny<0 or ny>=N or nx<0 or nx>=N):
            continue
        if(chk[ny][nx]):
            continue
        chk[ny][nx]=1
        solve(ny,nx,cur+1)
        chk[ny][nx]=0