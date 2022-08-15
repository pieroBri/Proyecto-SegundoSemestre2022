from typing_extensions import Self
from tablaMedica import TablaMedica


class Mascota:

    def __init__(self, id, nombre, especie, color, raza, nombreTutor, rutTutor, numeroTelefono, direccion, tablaMedica):
        self.nombre = nombre
        self.id = id
        self.especie = especie
        self.tablaMedica = tablaMedica
        self.color = color
        self.raza = raza
        self.nombreTutor = nombreTutor
        self.rutTutor = rutTutor
        self.numeroTelefono = numeroTelefono
        self.direccion = direccion
        self.tablaMedica:TablaMedica = tablaMedica

    def getId(self):
        return self.id
    
    def getNombreMascota(self):
        return self.nombre

    def getColorMascota(self):
        return self.color

    def getEspecie(self):
        return self.especie

    def getRaza(self):
        return self.raza

    def getNombreTutor(self):
        return self.nombreTutor

    def getRutTutor(self):
        return self.rutTutor

    def getNumeroTelefono(self):
        return self.numeroTelefono

    def getDireccion(self):
        return self.direccion

    #metodos de bajada para la tabla

    def agregarTablaMedica(self, tablaMedica):
        self.tablaMedica = tablaMedica

    def setAlergias(self, alergias):
        self.tablaMedica.setAlergias(alergias)
    
    def agregarAlergias(self, alergia):
        self.tablaMedica.agregarAlergias(alergia)
    
    def setRegistroDeOperaciones(self, operaciones):
        self.tablaMedica.setRegistroDeOperaciones(operaciones)
    
    def agregarOperaciones(self, operacion):
        self.tablaMedica.agregarOperaciones(operacion)

    def setRegistroDeVacunas(self, vacunas):
        self.tablaMedica.setRegistroDeVacunas(vacunas)
    
    def agregarVacunas(self, vacuna):
        self.tablaMedica.agregarVacunas(vacuna)

    #metodos de bajada para la tabla

    #metodos de subida para tabla

    def getAlergias(self):
        return self.tablaMedica.getAlergias()
    
    def getRegistroDeOperaciones(self):
        return self.tablaMedica.getRegistroDeOperaciones()

    def getVacunasSuministradas(self):
        return self.tablaMedica.getVacunasSuministradas()


    #metodos de subida para tabla

    # metodos de bajada para ficha

    def setIdFicha(self, idFicha): 
        self.tablaMedica.setIdFicha(idFicha)
    
    def setSucursalVeterinariaFicha(self, sucursalVeterinaria):
        self.tablaMedica.setSucursalVeterinariaFicha(sucursalVeterinaria)
    
    def setVeterinarioACargoFicha(self, veterinarioACargo):
        self.tablaMedica.setVeterinarioACargoFicha(veterinarioACargo)

    def setFechaConsultaFicha(self, fechaConsulta):
        self.tablaMedica.setFechaConsultaFicha(fechaConsulta)
    
    def setFrecRespiratoriaFicha(self, frecRespiratoria):
        self.tablaMedica.setFrecRespiratoriaFicha(frecRespiratoria)
    
    def setFrecCardiacaFicha(self, frecCardiaca):
        self.tablaMedica.setFrecCardiacaFicha(frecCardiaca)
    
    def setPesoFicha(self, peso):
        self.tablaMedica.setPesoFicha(peso)

    def setEdadFicha(self, edad):
        self.tablaMedica.setEdadFicha(edad)

    def setTempFicha(self, temp):
        self.tablaMedica.setTempFicha(temp)

    def setFichaDeOperacion(self, opFicha, idFicha): #se ocupa el id para identificar la ficha especifica a la que añadir
        self.tablaMedica.setFichaDeOperacion(opFicha)
    
    def setFichaDeHospitalizacion(self, hospFicha, idFicha): #se ocupa el id para identificar
        self.tablaMedica.setFichaDeHospitalizacion(hospFicha)
    
    def setFichaDeSefacion(self, sedFicha, idFicha): #se ocupa el id
        self.tablaMedica.setFichaDeSefacion(sedFicha)
    
    def setOperacionFicha(self, operacion): #indicadores de que existe una ficha de cada tipo
        self.tablaMedica.setOperacionFicha(operacion)
    
    def setHospitalizacionFicha(self, hospitalizacion):
        self.tablaMedica.setHospitalizacionFicha(hospitalizacion)

    def setSedacionFicha(self, sedacion):
        self.tablaMedica.setSedacionFicha(sedacion)

    # metodos de subida para ficha

    def getIdFicha(self, idFicha):
        self.tablaMedica.getIdFicha(idFicha)
    
    def getSucursalVeterinaria(self, idFicha):
        self.tablaMedica.getSucursalVeterinaria(idFicha)

    def getTemp(self, idFicha):
        self.tablaMedica.getTemp(idFicha)

    def getVeterinarioACargo(self, idFicha):
        self.tablaMedica.getVeterinarioACargo(idFicha)

    def getFechaConsulta(self, idFicha):
        self.tablaMedica.getFechaConsulta(idFicha)

    def getMedicamentosConsulta(self, idFicha):
        self.tablaMedica.getMedicamentosConsulta(idFicha)

    def getOperacion(self, idFicha):
        self.tablaMedica.getOperacion(idFicha)

    def getOperacionFicha(self, idFicha):
        self.tablaMedica.getOperacionFicha(idFicha)
    
    def getVacunasSuministradasConsulta(self, idFicha):
        self.tablaMedica.getVacunasSuministradasConsulta(idFicha)

    def getFrecRespiratoria(self, idFicha):
        self.tablaMedica.getFrecRespiratoria(idFicha)
    
    def getFrecCardiaca(self, idFicha):
        self.tablaMedica.getFrecCardiaca(idFicha)
    
    def getPeso(self, idFicha):
        self.tablaMedica.getPeso(idFicha)
    
    def getEdad(self, idFicha):
        self.tablaMedica.getEdad(idFicha)
    
    def getHospitalizacion(self, idFicha):
        self.tablaMedica.getHospitalizacion(idFicha)
    
    def getHospitalizacionFicha(self, idFicha):
        self.tablaMedica.getHospitalizacionFicha(idFicha)
    
    def getSedacion(self, idFicha):
        self.tablaMedica.getSedacion(idFicha)
    
    def getSedacioFicha(self, idFicha):
        self.tablaMedica.getSedacioFicha(idFicha)
    
    def getTratamiento(self, idFicha):
        self.tablaMedica.getTratamiento(idFicha)

    """def setOpFichaLocal(self, idFicha, opDicc, operacion):
        self.tablaMedica.setOpFichaLocal(idFicha, opDicc, operacion)

    def setVacFichaLocal(self, idFicha, vacDicc):
        self.tablaMedica.setVacFichaLocal(idFicha, vacDicc)

    def setHospFichaLocal(self, idFicha, hospFicha, hosp):
        self.tablaMedica.setHospFichaLocal(idFicha, hospFicha, hosp)

    def setSedFichaLocal(self, idFicha, sedDicc, sedacion):
        self.tablaMedica.setSedFichaLocal(idFicha, sedDicc, sedacion)

    def setTratamientoLocal(self, idFicha, tratamiento):
        self.tablaMedica.setTratamientoLocal(idFicha, tratamiento)

    def setMedicamentosConsultaLocal(self, idFicha, medicamentos):
        self.tablaMedica.setMedicamentosConsultaLocal(idFicha, medicamentos)

    def setRegistroDeOperaciones(self, operacion):
        self.tablaMedica.setRegistroDeOperacionesTrue(operacion)
        print(operacion)
    
    def setRegistroDeVacunas(self, vacuna):
        self.tablaMedica.setRegistroDeVacunasTrue(vacuna)

    def setRegistroAlergias(self, alergias):
        self.tablaMedica.setAlergiasTrue(alergias)

    #def editarInfoBasicaMascota(self):
        #pass

    def crearFichaMedicaConsulta(self,fichaMedica):
        pass

    # def editarFichaMedicaConsulta(self,fichaMedica):
    #     pass

    def buscarFichaMedicaConsulta(self):
        pass"""

    # def validarFormatoDatosFichaMedicaGeneral():
    #     pass

    # def validarFormatoDatosFichaMedica():
    #     pass

    # def solicitudServCrear():
    #     pass

    # def solicitudServEditar():
    #     pass

    def getId(self):
        return self.id

    def getTablaMedica(self) -> TablaMedica:
        return self.tablaMedica
    
    def getNombreMascota(self):
        return self.nombre

    def getColorMascota(self):
        return self.color

    def getEspecie(self):
        return self.especie

    def getRaza(self):
        return self.raza

    def getNombreTutor(self):
        return self.nombreTutor

    def getRutTutor(self):
        return self.rutTutor

    def getNumeroTelefono(self):
        return self.numeroTelefono

    def getDireccion(self):
        return self.direccion
    #faltan Getter y Setters