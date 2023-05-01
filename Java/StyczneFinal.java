import umontreal.iro.lecuyer.functions.MathFunction;
import umontreal.iro.lecuyer.functions.MathFunctionUtil;

public class StyczneFinal {
    public static double epsilon = 0.000000000000000000001;

    public static void Styczne(double a, double b) {
        funk fx = new funk();
        double x0 = 0;
        double x;
        if (fx.evaluate(a) * MathFunctionUtil.derivative(fx, a, 2) > 0) x0 = a;
        if (fx.evaluate(b) * MathFunctionUtil.derivative(fx, b, 2) > 0) x0 = b;
        int iter = 0;
        do {
            x = x0 - (fx.evaluate(x0) / MathFunctionUtil.derivative(fx, x0));
            x0 = x;
            iter++;

        } while (Math.abs(fx.evaluate(x)) > epsilon);
        System.out.println("Liczba iteracji: " + iter);
        System.out.println(x);
    }
    public static void main(String[]args){
        Styczne(-1.5,-0.75);
    }
}
    class funki implements MathFunction {

    @Override
    public double evaluate(double v) {
        return (v+1)*(Math.pow((v-1),4));
    }
}
