PGraphics pg;

void setup()
{
 size(1000,1000);
 pg = createGraphics(1000,1000);
 pg.beginDraw();
}

void draw()
{
  background(255);
   
  textSize(32);
  textAlign(CENTER);
  textMode(SHAPE);
  
  rectMode(CENTER);
  ellipseMode(CENTER);
  
  fill(255,255,255);
  rect(500, 100, 200, 100);
  fill(0, 0, 0);
  text("Get random battery", 500, 100, 200, 100);
  
  fill(255,255,255);
  rect(500, 300, 200, 100);
  fill(0,0,0);
  text("Find closest house", 500, 300, 200, 100);
  
  fill(255,255,255);
  rect(500,500,200,100);
  fill(0,0,0);
  text("Connect", 500, 500, 200, 100);
  
  fill(255,255,255);
  ellipse(500,700,200,100);
  fill(0,0,0);
  text("More houses?", 500, 700, 200, 100);
  
  fill(255);
  rect(500,900,200,100);
  fill(0);
  text("Done!",500, 900, 200, 100);
  


  pg.endDraw();
  image(pg, 0, 0);
  save("try.png");
}
