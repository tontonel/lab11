from infrastructure.departamentRepository import DepartamentRepository
from domain.departament import Departament
from domain.patient import Patient


def examples():
    """
    returns data examples
    :return:
    """
    return DepartamentRepository([Departament("dep1", 13, [Patient("Pop", "Andrei", "5020304234345", "cancer"),
                                                          Patient("David", "Maria", "2970616082645", "covid"),
                                                          Patient("Paraschiv", "Stefan", "1770816235356", "tuberculosis")]),
                                 Departament("dep2", 10,  [Patient("Marinscu", "Sorana", "6060903657897", "covid"),
                                                          Patient("Paraschiv", "Raul", "5031121295866", "blastoma"),
                                                          Patient("Enache", "Paul", "1981117381227", "covid"),
                                                          Patient("Tudosie", "Mariana", "1980507387664", "SIDA"),
                                                          Patient("Serban", "Anca", "2900805525414", "flu")]),
                                  Departament("dep3", 20, [Patient("Nicusor", "Emil", "1980507387664", "cancer"),
                                                          Patient("Eugenia", "Diana", "2960102510915", "covid"),
                                                          Patient("Sandra", "Dinu", "6020921465064", "covid"),
                                                          Patient("Costel", "Virgil", "1600102022999", "malaria"),
                                                          Patient("Stefanescu", "Anca", "2700113027943", "covid"),
                                                          Patient("Baltazar", "Olimpiu", "1300113025387", "hypertension"),
                                                          Patient("Suceava", "Roxana", "2550113022071", "cancer")]),
                                  Departament("dep4", 5, [Patient("Cristescu", "Marcel", "1900113020714", "parkinson"),
                                                          Patient("Bratian", "Calin", "5000113021986", "covid")])])



