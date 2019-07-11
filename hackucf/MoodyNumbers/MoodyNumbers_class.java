// Decompiled using: fernflower
// Took: 31ms

import java.nio.ByteBuffer;
import java.util.Scanner;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

class MoodyNumbers {
   public static void main(String[] var0) {
      Scanner var1 = new Scanner(System.in);
      NumberChecker var2 = new NumberChecker();
      System.out.println("Greetings, human! I am the Moody Number Bot.");
      sleep(1000);
      System.out.println("We're going to play a little game.");
      sleep(1000);
      System.out.println("Here's how it's going to go:");
      sleep(1000);
      System.out.println("I'm going to ask you to show me a number, and you're going to enter it in here.");
      sleep(1000);
      System.out.println("If you don't give me the right number, I'm going to get so angry that I stop talking to you.");
      sleep(1000);
      System.out.println("So don't give me the wrong numbers.");
      sleep(1000);
      System.out.println("Now that we've got that out of the way, let's begin!");
      sleep(1000);
      System.out.print("Show me a number that makes me happy: ");
      int var3 = var1.nextInt();
      if (!var2.isHappy(var3)) {
         wrongNumber("THAT NUMBER DOES NOT MAKE ME HAPPY!!!");
      }

      System.out.println("Ah, that number fills me with joy! Good one!");
      sleep(1000);
      System.out.println("Okay, I have another request for you.");
      sleep(1000);
      System.out.print("I'm in the mood to be scared. Frighten me with a number: ");
      int var4 = var1.nextInt();
      if (!var2.isScary(var4)) {
         wrongNumber("IS THAT THE BEST YOU HAVE? THAT COULDN'T SCARE AN INFANT!!!");
      }

      System.out.println("AAAAAHHH!!! That was scary! I think I accidentally overflowed my buffer!");
      sleep(1000);
      System.out.print("Give me a number that reminds me of my childhood: ");
      int var5 = var1.nextInt();
      if (var5 == 0) {
         wrongNumber("HOW DARE YOU INSULT MY CHILDHOOD!!!");
      } else if (!var2.isNostalgic(var5)) {
         wrongNumber("THIS NUMBER REMINDS ME OF THE TIME A MEAN HACKER ALMOST FRIED MY CIRCUITS, NOT MY CHILDHOOD!!!");
      }

      System.out.println("That number brings back memories of the time I received my first UDP packet!");
      sleep(1000);
      System.out.print("Now I want a number that arouses my circuits: ");
      int var6 = var1.nextInt();
      if (!var2.isArousing(var6)) {
         wrongNumber("THAT NUMBER IS SUCH A TURN-OFF THAT IT DISABLED MY NETWORK ADAPTER!!!");
      }

      System.out.println("Oooh, baby, that's a sexy number!");
      sleep(1000);
      System.out.println("Okay, you win. Here's your stupid flag. Goodbye.");
      sleep(1000);
      String var7 = getFlag(var3, var5, var4, var6);
      System.out.println(var7);
      var1.close();
   }

   static void sleep(int var0) {
      try {
         Thread.sleep((long)var0);
      } catch (InterruptedException var2) {
         ;
      }

   }

   static void wrongNumber(String var0) {
      System.out.println(var0 + " GET AWAY FROM ME!!!");
      System.exit(1);
   }

   static String getFlag(int var0, int var1, int var2, int var3) {
      byte[] var4 = ByteBuffer.allocate(16).putInt(var0).putInt(var1).putInt(var2).putInt(var3).array();
      SecretKeySpec var5 = new SecretKeySpec(var4, "AES");

      try {
         Cipher var6 = Cipher.getInstance("AES");
         var6.init(2, var5);
         byte[] var7 = new byte[]{-70, 76, 66, -121, -86, -83, 121, 99, 64, 57, 38, 57, -126, 78, 41, -27, 81, 64, 106, 78, -85, 104, 2, -119, 57, 115, -48, 104, -110, 45, -12, 92, 89, -101, 49, 15, 22, 122, -71, -77, -8, 23, -102, 46, -31, 81, 60, -44};
         byte[] var8 = var6.doFinal(var7);
         return new String(var8);
      } catch (Exception var9) {
         System.out.println("An error occurred: " + var9);
         return "ERROR";
      }
   }
}
