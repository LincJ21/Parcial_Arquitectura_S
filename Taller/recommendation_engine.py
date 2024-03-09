class RecommendationEngine:
    def recommend_benefits(self, user):
        # Lógica para recomendar beneficios
        pass

class BasicRecommendationEngine(RecommendationEngine):
    def recommend_benefits(self, user):
        # Implementación básica de recomendación de beneficios
        recommended_benefits = []

        # Lógica para recomendar beneficios básicos
        if user.age < 30:
            recommended_benefits.append("Descuentos en actividades recreativas")
        else:
            recommended_benefits.append("Descuentos en servicios de salud")

        return recommended_benefits

class AdvancedRecommendationEngine(RecommendationEngine):
    def recommend_benefits(self, user):
        # Implementación avanzada de recomendación de beneficios
        recommended_benefits = []

        # Lógica para recomendar beneficios avanzados
        if user.income > 50000:
            recommended_benefits.append("Acceso a servicios premium")
        else:
            recommended_benefits.append("Descuentos en compras en línea")

        return recommended_benefits
