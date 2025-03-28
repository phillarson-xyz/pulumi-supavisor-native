// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class Tenant extends pulumi.CustomResource {
    /**
     * Get an existing Tenant resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Tenant {
        return new Tenant(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'supavisor-native:tenants:Tenant';

    /**
     * Returns true if the given object is an instance of Tenant.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Tenant {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Tenant.__pulumiType;
    }

    /**
     * SELECT rolname, rolpassword FROM pg_authid WHERE rolname=$1
     */
    public /*out*/ readonly authQuery!: pulumi.Output<string | undefined>;
    /**
     * Database name
     */
    public /*out*/ readonly dbDatabase!: pulumi.Output<string>;
    /**
     * Database host
     */
    public /*out*/ readonly dbHost!: pulumi.Output<string>;
    /**
     * Database port
     */
    public /*out*/ readonly dbPort!: pulumi.Output<number>;
    public /*out*/ readonly enforceSsl!: pulumi.Output<boolean | undefined>;
    /**
     * External ID
     */
    public readonly externalId!: pulumi.Output<string | undefined>;
    public /*out*/ readonly insertedAt!: pulumi.Output<string | undefined>;
    /**
     * auto
     */
    public /*out*/ readonly ipVersion!: pulumi.Output<string | undefined>;
    public /*out*/ readonly requireUser!: pulumi.Output<boolean | undefined>;
    /**
     * your.domain.com
     */
    public /*out*/ readonly sniHostname!: pulumi.Output<string | undefined>;
    public readonly tenant!: pulumi.Output<outputs.tenants.TenantProperties>;
    public /*out*/ readonly updatedAt!: pulumi.Output<string | undefined>;
    public /*out*/ readonly upstreamSsl!: pulumi.Output<boolean | undefined>;
    /**
     * none
     */
    public /*out*/ readonly upstreamVerify!: pulumi.Output<string | undefined>;
    public /*out*/ readonly users!: pulumi.Output<outputs.tenants.User[]>;

    /**
     * Create a Tenant resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TenantArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.tenant === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tenant'");
            }
            resourceInputs["externalId"] = args ? args.externalId : undefined;
            resourceInputs["tenant"] = args ? (args.tenant ? pulumi.output(args.tenant).apply(inputs.tenants.tenantPropertiesArgsProvideDefaults) : undefined) : undefined;
            resourceInputs["authQuery"] = undefined /*out*/;
            resourceInputs["dbDatabase"] = undefined /*out*/;
            resourceInputs["dbHost"] = undefined /*out*/;
            resourceInputs["dbPort"] = undefined /*out*/;
            resourceInputs["enforceSsl"] = undefined /*out*/;
            resourceInputs["insertedAt"] = undefined /*out*/;
            resourceInputs["ipVersion"] = undefined /*out*/;
            resourceInputs["requireUser"] = undefined /*out*/;
            resourceInputs["sniHostname"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
            resourceInputs["upstreamSsl"] = undefined /*out*/;
            resourceInputs["upstreamVerify"] = undefined /*out*/;
            resourceInputs["users"] = undefined /*out*/;
        } else {
            resourceInputs["authQuery"] = undefined /*out*/;
            resourceInputs["dbDatabase"] = undefined /*out*/;
            resourceInputs["dbHost"] = undefined /*out*/;
            resourceInputs["dbPort"] = undefined /*out*/;
            resourceInputs["enforceSsl"] = undefined /*out*/;
            resourceInputs["externalId"] = undefined /*out*/;
            resourceInputs["insertedAt"] = undefined /*out*/;
            resourceInputs["ipVersion"] = undefined /*out*/;
            resourceInputs["requireUser"] = undefined /*out*/;
            resourceInputs["sniHostname"] = undefined /*out*/;
            resourceInputs["tenant"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
            resourceInputs["upstreamSsl"] = undefined /*out*/;
            resourceInputs["upstreamVerify"] = undefined /*out*/;
            resourceInputs["users"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Tenant.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Tenant resource.
 */
export interface TenantArgs {
    /**
     * External ID of the tenant
     */
    externalId?: pulumi.Input<string>;
    tenant: pulumi.Input<inputs.tenants.TenantPropertiesArgs>;
}
