mport java.math.BigInteger;
import java.security.MessageDigest;

public class NumberChecker {
    public NumberChecker() {
        super();
    }
    
    public boolean isHappy(int n) {
        if (n % 270719 != 0) {
            return false;
        }
        n /= 270719;
        return n == 6317;
    }
    
    public boolean isScary(final int n) {
        return (n & 0xFF) == 0x0 && n >> 12 == 0 && (n >> 8 ^ 0xF) == 0x4;
    }
    
    public boolean isNostalgic(final int n) {
        try {
            return String.format("%032x", new BigInteger(1, MessageDigest.getInstance("MD5").digest(Integer.toString(n).getBytes("UTF-8")))).equals("08ef85248841b7fbf4b1ef8d1090a0d4");
        }
        catch (Exception ex) {
            System.out.println("An error occurred: " + ex);
            return false;
        }
    }
    
    public boolean isArousing(int n) {
        final int n2 = n % 10;
        n /= 10;
        final int n3 = n % 10;
        n /= 10;
        if (n3 % 2 != 0) {
            return false;
        }
        if (n2 != n3 / 2 * 3) {
            return false;
        }
        for (int i = 0; i < 3; ++i) {
            if (n % 10 != n2) {
                return false;
            }
            n /= 10;
            if (n % 10 != n3) {
                return false;
            }
            n /= 10;
        }
        return n == 0 && n2 % 2 != 0 && (n2 ^ n3) == 0xF;
    }
}

