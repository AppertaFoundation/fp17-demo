from django import forms


class PartOne(forms.Form):
    patient_nhs_number = forms.IntegerField()

    provider_name = forms.CharField()
    provider_location_number = forms.IntegerField()

    provider_address = forms.CharField()

    performer_number_same_as_provider = forms.BooleanField(required=False)
    provider_number = forms.IntegerField()


class PartTwo(forms.Form):
    title = forms.CharField()
    forenames = forms.CharField()
    surname = forms.CharField()

    gender = forms.ChoiceField(choices=(
        ('male', "Male"),
        ('female', "Female"),
    ))

    date_of_birth = forms.DateField()

    house_number_or_name = forms.CharField()
    street = forms.CharField()
    city_or_town = forms.CharField()
    county = forms.CharField()
    postcode = forms.CharField()


class PartThree(forms.Form):
    incomplete_treatment_band_1 = forms.BooleanField(required=False)
    incomplete_treatment_band_2 = forms.BooleanField(required=False)
    incomplete_treatment_band_3 = forms.BooleanField(required=False)

    date_of_acceptance = forms.DateField()
    completion_same_as_acceptance_date = forms.BooleanField(required=False)
    completion_or_last_visit = forms.DateField()


class PartFour(forms.Form):
    patient_under_18 = forms.BooleanField(required=False)
    full_remission_hc2_cert = forms.BooleanField(required=False)
    partial_remission_hc3_cert = forms.BooleanField(required=False)
    expectant_mother = forms.BooleanField(required=False)
    nursing_mother = forms.BooleanField(required=False)
    aged_18_in_full_time_education = forms.BooleanField(required=False)
    income_support = forms.BooleanField(required=False)
    nhs_tax_credit_exemption = forms.BooleanField(required=False)
    income_based_jobseekers_allowance = forms.BooleanField(required=False)
    pension_credit_guarantee_credit = forms.BooleanField(required=False)
    prisoner = forms.BooleanField(required=False)
    income_related_employment_and_support_allowance = forms.BooleanField(required=False)
    universal_credit = forms.BooleanField(required=False)
    evidence_of_exception_or_remission_seen = forms.BooleanField(required=False)

    patient_charge_collected = forms.DecimalField(decimal_places=2)


class PartFive(forms.Form):
    treatment_category_band_1 = forms.BooleanField(required=False)
    treatment_category_band_2 = forms.BooleanField(required=False)
    treatment_category_band_3 = forms.BooleanField(required=False)
    urgent_treatment = forms.BooleanField(required=False)
    regulation_11_replacement_appliance = forms.BooleanField(required=False)
    prescription_only = forms.BooleanField(required=False)
    denture_repairs = forms.BooleanField(required=False)
    bridge_repairs = forms.BooleanField(required=False)
    arrest_of_bleeding = forms.BooleanField(required=False)
    removal_of_sutures = forms.BooleanField(required=False)


class PartFiveA(forms.Form):
    scale_and_polish = forms.BooleanField(required=False)
    fluoride_varnish = forms.BooleanField(required=False)
    fissure_sealants = forms.IntegerField()
    radiographs_taken = forms.IntegerField()

    endodontic_treatment = forms.BooleanField(required=False)
    permanent_fillings_and_sealant_restorations = forms.IntegerField()
    extractions = forms.IntegerField()
    crowns_provided = forms.IntegerField()

    upper_denture_acrylic = forms.IntegerField()
    lower_denture_acrylic = forms.IntegerField()
    upper_denture_metal = forms.IntegerField()
    lower_denture_metal = forms.IntegerField()

    veneers_applied = forms.IntegerField()
    inlays = forms.IntegerField()
    bridges_fitted = forms.IntegerField()
    referral_for_advanced_mandatory_services_band = forms.IntegerField()

    examination = forms.BooleanField(required=False)
    antibiotic_items_prescribed = forms.IntegerField()
    other_treatment = forms.BooleanField(required=False)
    best_practice_prevention_according_to_delivering_better_oral_health_offered = forms.BooleanField(required=False)

    decayed_teeth_permanent = forms.IntegerField()
    decayed_teeth_deciduous = forms.IntegerField()
    missing_teeth_permanent = forms.IntegerField()
    missing_teeth_deciduous = forms.IntegerField()
    filled_teeth_permanent = forms.IntegerField()
    filled_teeth_deciduous = forms.IntegerField()

class PartSix(forms.Form):
    treatment_on_referral = forms.BooleanField(required=False)
    free_repair_or_replacement = forms.BooleanField(required=False)
    further_treatment_within_2_months = forms.BooleanField(required=False)
    domicillary_services = forms.BooleanField(required=False)
    sedation_services = forms.BooleanField(required=False)


class PartSeven(forms.Form):
    number_of_months = forms.IntegerField()


class PartEight(forms.Form):
    field_1 = forms.CharField()
    field_2 = forms.CharField()
    field_3 = forms.CharField()
    field_4 = forms.DecimalField(decimal_places=2)


class PartNine(forms.Form):
    necessary_care_provided = forms.BooleanField(required=False)
    necessary_care_carried_out = forms.BooleanField(required=False)

    signature = forms.CharField()
    signature_date = forms.DateField()
