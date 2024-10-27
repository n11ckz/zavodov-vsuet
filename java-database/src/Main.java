import database.Database;
import data.*;
import utils.Console;

public class Main {
    public static void main(String[] args) {
        Console console = new Console();
        Database database = new Database(console);
        DataFactory factory = new DataFactory(console);

        Application application = new Application(database, factory, console);
        application.Run();
    }
}