
import java.util.*;
import java.security.MessageDigest;
import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;


public class cashemodd {
    public static String bin2hex(byte[] bArr) {
        if (bArr == null) {
            return null;
        }
        int length = bArr.length;
        String str = "";
        for (int i = 0; i < length; i++) {
            if ((bArr[i] & 255) < 16) {
                StringBuilder outline37 = outline37(str, "0");
                outline37.append(Integer.toHexString(bArr[i] & 255));
                str = outline37.toString();
            } else {
                StringBuilder outline34 = outline34(str);
                outline34.append(Integer.toHexString(bArr[i] & 255));
                str = outline34.toString();
            }
        }
        return str;
    }

    public static String decrypt(String str, String str2, String str3, String str4) throws Exception {
        SecretKeySpec secretKeySpec = new SecretKeySpec(SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1").generateSecret(new PBEKeySpec(str4.toCharArray(), hex2bin(str), 1024, 256)).getEncoded(), "AES");

        byte[] hex2bin = hex2bin(str2);
        new String(hex2bin);
        IvParameterSpec ivParameterSpec = new IvParameterSpec(hex2bin);
        Cipher instance = Cipher.getInstance("AES/CBC/PKCS5Padding");
        instance.init(2, secretKeySpec, ivParameterSpec);
        return new String(instance.doFinal(hex2bin(str3)));
    }

    public static String encrypt(String str, String str2, String str3, String str4) throws Exception {
        SecretKeySpec secretKeySpec = new SecretKeySpec(SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1").generateSecret(new PBEKeySpec(str4.toCharArray(), hex2bin(str), 1024, 256)).getEncoded(), "AES");
        String re = new String(String.valueOf(new PBEKeySpec(str4.toCharArray(), hex2bin(str), 1024, 256)));
        byte[] hex2bin = hex2bin(str2);
        new String(hex2bin);
        IvParameterSpec ivParameterSpec = new IvParameterSpec(hex2bin);
        Cipher instance = Cipher.getInstance("AES/CBC/PKCS5Padding");
        instance.init(1, secretKeySpec, ivParameterSpec);
        return new String(bin2hex(instance.doFinal(str3.getBytes())));
    }

    public static byte[] hex2bin(String str) {
        if (str == null || str.length() < 2) {
            return null;
        }
        int length = str.length() / 2;
        byte[] bArr = new byte[length];
        for (int i = 0; i < length; i++) {
            int i2 = i * 2;
            bArr[i] = (byte) Integer.parseInt(str.substring(i2, i2 + 2), 16);
        }
        return bArr;
    }

    public static StringBuilder outline37(String str, String str2) {
        StringBuilder sb = new StringBuilder();
        sb.append(str);
        sb.append(str2);
        return sb;
    }

    public static StringBuilder outline34(String str) {
        StringBuilder sb = new StringBuilder();
        sb.append(str);
        return sb;
    }

    public static void main(String[] args) {

        try {
            String l = args[0];
            String m = args[1];
            String n = args[2];
            String o = args[3];
            System.out.println(new String(encrypt(l, m, n, o)));

        } catch (Exception e){
            e.printStackTrace();
        }

//         System.out.println(new String(decrypt(l, m, n, o)));
    }
}